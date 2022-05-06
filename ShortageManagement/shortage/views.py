# Create your views here.
from __future__ import division
from cgitb import html
from io import StringIO
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.utils import OperationalError
from django.contrib import messages
import pandas as pd
import psycopg2
from datetime import datetime
import pathlib
from shortage.forms import Myform,Form
from django.db.models import Q
from .decorators import allowed_users
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from administration.templates import administration



# from shortage.models import MB52,SE16N_CEPC,SE16N_T001L,SE16N_T024,ZMM_CARNET_CDE_IS,ZRPFLG13,ZPP_MD_Stock,Core,CoreHistory,Stock_transit,MDMA,ART_MARA_MARC
from shortage.models import *
#function to upload files


def upload(request):
    #Delete all data before upload
    MB52.objects.all().delete()
    SE16N_CEPC.objects.all().delete()
    SE16N_T001L.objects.all().delete()
    SE16N_T024.objects.all().delete()
    ZMM_CARNET_CDE_IS.objects.all().delete()
    Stock_transit.objects.all().delete()
    MDMA.objects.all().delete()
    ART_MARA_MARC.objects.all().delete()
    ZPP_MD_Stock.objects.all().delete()
    uploaded_files(request)  #call function to upload files
    return redirect ('files_list')

#Upload Files and check if exist   
def uploaded_files(request):
    #connection to DB 
        try:
            conn= psycopg2.connect(host='localhost', dbname='latecoere_db', user='postgres', password='sahar',port='5432') 
            file_mb52=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\MB52 ALL.xlsx')
            file_se16ncepc=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\cepc.xlsx')
            file_se16nt001l=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\T001l.xlsx')
            file_se16nt024=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\T024.xlsx')
            file_zmm=pathlib.Path( r'C:\Users\bibas\Downloads\Input SAP\ZMM_CARNET_CDE_IS.xlsx')
            file_st=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\stock_transit.xlsx')
            file_art=pathlib.Path( r'C:\Users\bibas\Downloads\Input SAP\ART_MARA_MARC_GLOBAL_202214.xlsx')
            file_md=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\MDMA.xlsx')
            zpp_md_stock={
                "2500":r"C:\Users\bibas\Downloads\Input SAP\BEL MD STOCK.xlsx",
                "2600":r"C:\Users\bibas\Downloads\Input SAP\CAN MD STOCK.xlsx",
                "2400":r"C:\Users\bibas\Downloads\Input SAP\CAS MD STOCK.xlsx",
                "2010":r"C:\Users\bibas\Downloads\Input SAP\COL MD STOCK.xlsx",
                "2110":r"C:\Users\bibas\Downloads\Input SAP\FOU MD STOCK.xlsx",
                "2200":r"C:\Users\bibas\Downloads\Input SAP\HBG MD STOCK.xlsx",
                "2000":r"C:\Users\bibas\Downloads\Input SAP\LAB MD STOCK.xlsx",
                "2030":r"C:\Users\bibas\Downloads\Input SAP\LEC MD STOCK.xlsx",
                "2020":r"C:\Users\bibas\Downloads\Input SAP\LIP MD STOCK.xlsx",
                "2300":r"C:\Users\bibas\Downloads\Input SAP\MEX MD STOCK.xlsx"
            } 

            #User name
            uploded_by =1
            #Date time for upload files
            uploded_at = datetime.now()
            #year
            year=datetime.now().year
            #week
            week=datetime.now().strftime("%W")
            #control statment to check if files exists    
            if (file_mb52.exists()   and  file_se16ncepc.exists() and file_se16nt001l.exists() and file_se16nt024.exists() and file_zmm.exists() and file_st.exists() and file_art.exists() and file_md.exists()):
                import_file_MB52(conn,file_mb52,year,week,uploded_by,uploded_at)
                import_file_SE16N_CEPC(conn,file_se16ncepc,year,week,uploded_by,uploded_at)
                import_file_SE16N_T001L(conn,file_se16nt001l,year,week,uploded_by,uploded_at)
                import_file_SE16N_T024(conn,file_se16nt024,year,week,uploded_by,uploded_at)
                import_file_ZMM_CARNET_CDE_IS(conn,file_zmm,year,week,uploded_by,uploded_at)
                for division,file in zpp_md_stock.items():
                    import_file_ZPP_MD_Stock(conn,division,file,year,week,uploded_by,uploded_at)
                import_file_Stock_transit(conn,file_st,year,week,uploded_by,uploded_at)
                import_file_ART_MARA_MARC(conn,file_art,year,week,uploded_by,uploded_at)
                import_file_MDMA(conn,file_md,year,week,uploded_by,uploded_at)
            else:
                messages.error(request, 'Files not found')
        except OperationalError:
           messages.error(request,'Data base not found')

#function for import file MB52
def import_file_MB52(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #Convert Division and Store to int and fill nan with 0
    df['Division']=df['Division'].fillna(0)
    df['Division']=df['Division'].astype(int)
    df['Magasin']=df['Magasin'].fillna(0)
    df['Magasin']=df['Magasin'].astype(int)

    print(df)

    df=df.to_csv(index=False,header=None) #To convert to csv
    
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="shortage_mb52",
            columns=[
               'year',
               'week',
               'uploaded_by',
               'uploaded_at',
               'material',
               'division',
               'store', 
               'store_level_deletion_indicator',
               'unit',
               'for_free_use',	
               'currency',
               'value_free_use',
               'transit_transfer',
               'transit_transfer_value', 	
               'in_quality_control',
               'value_quality_control', 	
               'non_free_stock',	
               'non_free_value', 
               'blocked',
               'blocked_stock_value',
               'returns',	
               'blocked_return_stock_value',
            ],
            null='',
            sep=','
        )
    con.commit()
#function for Import file SE16N_CEPC
def import_file_SE16N_CEPC(con,file,year,week,username,uploaded_at):
        #Read file
        df = pd.read_excel(file,index_col=False) # to read file excel
        #insert 2 column year, week
        df.insert(0,'year',year,True)
        df.insert(1,'week',week,True)
        #insert 2 column created by, created at
        df.insert(2,'uploaded_by',username,True)
        df.insert(3,'uploaded_at',uploaded_at,True)
        print(df)
        df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
        
        se=StringIO()
        se.write(df)
        se.seek(0)
        with con.cursor() as curs:
            curs.copy_from(
                file=se,
                table="shortage_se16n_cepc",
                columns=[
                    'year',
                    'week',
                    'uploaded_by',
                    'uploaded_at',
                    'profit_center',
                    'valid_to',
                    'controlling_area', 
                    'valid_from',
                    'created_on',
                    'created_by',	
                    'field_name_of_CO_PA_characteristic',
                    'department',
                    'person_responsible_for_profit_center',
                    'user_responsible', 	
                    'currency',
                    'successor_profit_center', 	
                    'country_key',	
                    'title', 
                    'name1',
                    'name2',
                    'name3',	
                    'name4',
                    'city',
                    'district',
                    'street',
                    'po_box',	
                    'postal_code',
                    'p_o_box_costal_code',
                    'language_key',
                    'telebox_number',
                    'telephone1',
                    'telephone2',
                    'fax_number',	
                    'teletex_number',
                    'telex_number',
                    'data_line',
                    'printer_name',
                    'hierarchy_area',
                    'company_code',	
                    'joint_venture',
                    'recovery_indicator',
                    'equity_type',
                    'tax_jurisdiction',
                    'region',
                    'usage',
                    'application',
                    'procedure',	
                    'logical_system',
                    'lock_indicator',
                    'prctr_formula_planning_template',
                    'segment',
                    'name',
                    'long_text',	
                    'profit_center_short_text_for_matchcode',
                 ],
                null='',
                sep=';'
            )
        con.commit()
#function for Import file SE16N_T001L
def import_file_SE16N_T001L(con,file,year,week,username,uploaded_at):
    #     #Read file
    df = pd.read_excel(file,index_col=False) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #insert 2 column created by, created at
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
        
    se=StringIO()
    se.write(df)
    se.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=se,
            table="shortage_se16n_t001l",
            columns=[
                    'year',
                    'week',
                    'uploaded_by',
                    'uploaded_at',
                    'division',
                    'store',
                    'descr_of_storage_loc', 
                    'store_level_deletion_indicator',
                    'negative_inventory',
                    'fix_stk_theo',	
                    'mrp_code',
                    'authorization_check',
                    'stor_resource',
                    'management_missing_units', 	
                    'partner_store',
                    'sales_organization', 	
                    'distribution_channel',	
                    'shipping_point_receiving_pt', 
                    'vendor',
                    'customer',	
                    'business_system_of_mes',
                    'inventory_management_type',
                    'license_number',
                    'in_transit_assignment',
                    'tank_assgn',

                ],
            null='',
            sep=','
            )
    con.commit()
#function for Import file SE16N_T024
def import_file_SE16N_T024(con,file,year,week,username,uploaded_at):
      #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    SE24=StringIO()
    SE24.write(df)
    SE24.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=SE24,
            table="shortage_se16n_t024",
            columns=[
                'year',
                'week',
                'uploaded_by',
                'uploaded_at',
                'purchasing_group',
                'description_p_group',
                'tel_no_purch_group', 
                'output_device',
                'fax_number',	
                'telephone',
                'extension',
                'e_mail_address',
                'user_name', 	
            ],
            null='',
            sep=','
        )
    con.commit() 
#function for Import file ZMM_CARNET_CDE_IS
def import_file_ZMM_CARNET_CDE_IS(con,file,year,week,username,uploaded_at):
     #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #Convert Division and Store to int and fill nan with 0
    # df['Division']=df['Division'].fillna(0)
    # df['Division']=df['Division'].astype(int)
    df['Magasin']=df['Magasin'].fillna(0)
    df['Magasin']=df['Magasin'].astype(int)
     
    print(df)
    df=df.to_csv(index=False,header=None,sep='|') #To convert to csv
    
    zmm=StringIO()
    zmm.write(df)
    zmm.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zmm,
            table="shortage_zmm_carnet_cde_is",
            columns=[
                'year',
                'week',
                'uploaded_by',
                'uploaded_at',
                'request_no',
                'division',
                'store', 
                'purchase_document',
                'poste1',	
                'due_date',
                'vendor',
                'vendor_name',
                'material', 	
                'designation_add_material',
                'name',
                'transmission_info',
                'validated_by',
                'priority', 
                'quantity',
                'quantity_to_receive',	
                'date_of_purchase',
                'desired_date',
                'original_delivery_date',
                'contractual_delivery_date', 	
                'validated_delivery_date',
                'confirmed_quantity',
                'comment',
                'expected_stock_week_w',
                'expected_stock_week_w_1',
                'expected_stock_week_w_2',
                'expected_stock_week_w_3',
                'expected_stock_week_w_4',
                'expected_stock_week_w_5',
                'expected_stock_week_w_6',
                'expected_stock_week_w_7',
                'expected_stock_week_w_8',
                'expected_stock_week_w_9',
                'expected_stock_week_w_10',
                'expected_stock_week_w_11',
                'expected_stock_week_w_12',
                'confirmation',
                'estimated_delivery_time',
                'comment_vendor',
                'element_otp',
                'business_document',
                'poste2',
                'need_number',
                'net_price',
                'currency',
                'price_basis',
                'price_unit',
                'net_order_value',
                'purchasing_document_type',
                'exception_message_number',
                'exception_message',
                'purchasing_group',
            ],
            null='',
            sep='|'
        )
    con.commit() 

#function for Import file ZPP_MD_Stock
def import_file_ZPP_MD_Stock(con,division,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    df.insert(4,'division',division,True)
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    ZPP=StringIO()
    ZPP.write(df)
    ZPP.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=ZPP,
            table="shortage_zpp_md_stock",
            columns=[
                'year',
                'week',
                'uploaded_by',
                'uploaded_at',
                'division',
                'material',
                'plan_date',
                'mrp_element', 
                'data_for_planning_element',
                'action_message',	
                'Input_need',
                'available_quantity',
                'reorder_date',
                'vendor', 	
                'customer',
            ],
            null='',
            sep=','
        )
    con.commit() 

#function for Import file 
def import_file_Stock_transit(con,file,year,week,username,uploaded_at):
      #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
     
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    
    ST=StringIO()
    ST.write(df)
    ST.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=ST,
            table="shortage_stock_transit",
            columns=[
               'year',
               'week',
               'uploaded_by',
               'uploaded_at',
               'pExp',
               'taken_plant',
               'transfer_code', 
               'poscde',
               'tLvr',	
               'actual_sm',
               'delivery',
               'item',
               'num_picking_UUID', 	
               'num_parcel',
               'material', 
               'delivery_qty',
               'uq',
               'qty_delivered',
               'qty_received',
               'not_received',
               'customer_order', 
               'of_art_description',
               'msn',	
               'appro_Special',
               'comment',
               'n_of',
               'article_of', 
            ],
            null='',
            sep=','
        )
    con.commit() 
#function for import file ART_MARA_MARC
def import_file_ART_MARA_MARC(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)

    df=df.to_csv(index=False,header=None,sep=';') #To convert to csv
    
    art=StringIO()
    art.write(df)
    art.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=art,
            table="shortage_art_mara_marc",
            columns=[
               'year',
               'week',
               'uploaded_by',
               'uploaded_at',
               'material',
               'material_designation',
               'text_material', 
               'market_group',
               'division',
               'ctrpr',	
               'typ_app',
               'a_s',
               'tcy',
               'dfi', 	
               'dpr',
               'horiz', 	
               'mp',	
               'r', 
               'tyar',
               'nai',
               'i_c',	
               'aappr_def',
               'mgApp',
               'mag',
               'tl',
               'fixed_batch',
               'uq1',
               'security_stock', 
               'uq2',
               'tre',
               'gest',	
               'di',
               'scrap',
               'gac',
               'profile', 	
               'prpiat',
               'created_by', 	
               'language',	
               'created_on', 
               'gcha',
               'gs',
               'comparison_mode_of_the_requirements',	
               'int_adjustment_upstream',
               'int_adjustment_downstream',
               'size_l_min', 
               'uq3',
               'rounded_value',
               'uq4',	
               'lot_size_mx',
               'uq5',
               'maximum_stock',
               'uq6', 	
               'edge',
               'typ', 	
               'time_limit1',	
               'time_limit2', 
               'recipient_ctrl',
               'material_filled',
               'dv',	
               'gml',
               'grpi',
               'abc',
               'uq7',	
               'wbs_element',
               'grpa',
               'control_code',
               'product_hierarchy', 	
               'gross_weight',
               'unp1', 	
               'net_weight',	
               'unp2', 
               'no_ccr',
               'ccr_lot_size',
               'uq8',
            ],
            null='',
            sep=';'
        )
    con.commit()

#function for import file MDMA
def import_file_MDMA(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)

    df=df.to_csv(index=False,header=None) #To convert to csv
    
    md=StringIO()
    md.write(df)
    md.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=md,
            table="shortage_mdma",
            columns=[
               'year',
               'week',
               'uploaded_by',
               'uploaded_at',
               'material',
               'planning_unit',
               'division', 
               'planning_profile',
               'planning_type',
               'manager',	
               'planning_group',
               'order_point',
               'planning_rate',
               'fixed_planning_horizon', 	
               'lot_size_calculation_key',
               'rounding_profile', 	
               'rounding_value',	
               'minimum_lot_size', 
               'maximum_lot_size',
               'maximum_stock',
               'cycle',	
               'rejects_ss_ens',
               'special_supply',
               'production_store',
               'store_for_external_supply',
               'planning_calendar',
               'safety_stock',
               'coverage_profile', 
               'safety_stock_actual_stock',
               'fixed_lot_size',
               'fixed_lot_costs',	
               'storage_cost_code',
               'service_rate',
               'forecast_profile',
               'ref_cons_val', 	
               'un_plan_cons',
               'au', 	
               'multiplier',	
               'suppr_indicator', 
               'prof_per_sec',
               'dependent_needs_planner',
               'reset_auto',	
               'management_status',
               'correction_pow',
               'safety_time', 
               'for_apo',
               'forecast_delivery_time',
               'take_into_account_the_expected_delivery_time',	
            ],
            null='',
            sep=','
        )
    con.commit()

#CRUD CORE
def core(request):#show list of core 
    filter=""
    if  (request.method == 'POST') :
        data=Core.objects.all().order_by('-id')
        filter='all'
    else:
        data=Core.undeleted_objects.all().exclude(Q(status='Close') | Q(status='Refuse')).order_by('-id')
    return render(request,r'app\core.html',{'data':data,'filter':filter})

@allowed_users(allowed_roles=['users','administrators'])
def create_core(request):#create new core
    if  (request.method == 'POST') :
        material=request.POST['material']
        division=request.POST['division']
        data=Core.undeleted_objects.all().filter(material=material,division=division).exclude(status='Close')
        print(data.first())
        if data:
            messages.warning(request,'Core is already exist !')
            # return render(request,'app/core_history.html',{'pk':data.first().id,'data':data})
            return core_history(request,data.first().id)
        else:
            myform = Myform(request.POST)
            if myform.is_valid():
                instance=myform.save(commit=False)
                instance.created_on =datetime.now()
                instance.updated_on =datetime.now()
                instance.created_by=1
                instance.save()
                messages.success(request,'Core added sucessfully')
                return redirect('core')

    return render(request,'app\create_core.html',{'myform' : Myform})

@allowed_users(allowed_roles=['administrators'])
def update_core(request,pk): #function for update core
    core=Core.objects.get(id=pk)
    myform=Myform(instance=core)
    if (request.method=='POST'):
        myform = Myform(request.POST,instance=core)
        material=request.POST['material']
        division=request.POST['division']
        data=Core.undeleted_objects.all().filter(material=material,division=division).exclude(status='Close')
        print(data.first())
        if data:
            messages.warning(request,'Core is already exist !')
            # return render(request,'app/core_history.html',{'pk':data.first().id,'data':data})
            return core_history(request,data.first().id)
        else:
            if myform.is_valid():
                myform.save()
                messages.success(request,"Core updated successfully!")
                return redirect('core')
            else:
                messages.error(request, 'Invalid form submission.') 
    return render(request,'app/updateForm.html',{'core' : core,'myform' : myform})

@allowed_users(allowed_roles=['administrators'])
def delete_core(request,pk): #function soft-delete
    core=Core.objects.get(id=pk)
    core.deleted=True
    core.deleted_on=datetime.now()
    core.deleted_by=1
    core.save()
    return redirect('core')

def core_history(request,pk):
    data=CoreHistory.objects.all().filter(core_id=pk).order_by('-id')
    core=Core.objects.get(id=pk)
    return render(request,'app/core_history.html',{'form':Form,'pk':pk,'data':data,'core':core})


def save_core_history(request,pk):
    # data=CoreHistory.objects.all().filter(core_id=pk).order_by('-id')
    core=Core.objects.get(id=pk)
    if (request.method == 'POST'):
        core.status = request.POST['status']
    if core.status== 'Close':
        core.closing_date=datetime.now()
    core.save()
    form=Form(request.POST)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.created_on =datetime.now()
        instance.created_by='1'
        instance.core_id=pk
        instance.action=request.POST['status']
        instance.save()
    return redirect('core_history')

#overview
def overview(request):
    #Call all files
    data_zpp=ZPP_MD_Stock.objects.values('year','week','material','vendor','mrp_element','Input_need','available_quantity','division')
    data_zmm=ZMM_CARNET_CDE_IS.objects.values('year','week','material','validated_delivery_date','confirmed_quantity','purchasing_group','vendor_name','validated_delivery_date','contractual_delivery_date','division')
    data_mb52=MB52.objects.values('year','week','value_free_use','material','division','store')
    data_tl001l=SE16N_T001L.objects.values('year','week','descr_of_storage_loc','division','store')
    data_cepc=SE16N_CEPC.objects.values('year','week','district','profit_center')
    data_st=Stock_transit.objects.values('year','week','num_parcel','delivery_qty','material')
    data_mara_marc=ART_MARA_MARC.objects.values('year','week','tyar','mp','gac','a_s','typ','ctrpr','dpr','material','division')
    data_t024=SE16N_T024.objects.values('year','week','purchasing_group')
    data_mdma=MDMA.objects.values('year','week','forecast_delivery_time','planning_unit','material','division')

    #Convert to data frame
    df_zpp=pd.DataFrame(list(data_zpp))
    df_zmm=pd.DataFrame(list(data_zmm))
    df_mb52=pd.DataFrame(list(data_mb52))
    df_tl001l=pd.DataFrame(list(data_tl001l))
    df_cepc=pd.DataFrame(list(data_cepc))
    df_st=pd.DataFrame(list(data_st))
    df_mara_marc=pd.DataFrame(list(data_mara_marc))
    df_mdma=pd.DataFrame(list(data_mdma))
    df_t024=pd.DataFrame(list(data_t024))

    ##############################
    #MB52 and T001L
    ##############################
    #Add Key to DF
    df_mb52['key']=df_mb52['year'].astype(str)+df_mb52['week'].astype(str)+df_mb52['division'].astype(str)+df_mb52['store'].astype(str)
    df_tl001l['key']=df_tl001l['year'].astype(str)+df_tl001l['week'].astype(str)+df_tl001l['division'].astype(str)+df_tl001l['store'].astype(str)
    #Convert to Dict
    df_tl001l_dict=dict(zip(df_tl001l.key,df_tl001l.descr_of_storage_loc))
    #Get data from dict using map
    df_mb52['descr_of_storage_loc']=df_mb52['key'].map(df_tl001l_dict)
    
    #Delete dataframe not used
    
    ##############################
    #MARA MARC and T024
    ##############################
    #Add key to DF
    df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['gac'].astype(str)
    df_t024['key']=df_t024['year'].astype(str)+df_t024['week'].astype(str)+df_t024['purchasing_group'].astype(str)
    #Convert to Dict
    df_t024_dict=dict(zip(df_t024.key,df_t024.purchasing_group))    
    # #Get data from dict using map
    df_mara_marc['purchasing_group']=df_mara_marc['key'].map(df_t024_dict)
  
    #Delete dataframe not used

    ##############################
    #MARA MARC and  MDMA
    ##############################
    #Delete key
    # del df_mara_marc['key'] 
    # #Add  new key to DF mara_marc
    # df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['material'].astype(str)+df_mara_marc['division'].astype(str)
    # #Add key to DF
    # df_mdma['key']=df_mdma['year'].astype(str)+df_mdma['week'].astype(str)+df_mdma['material'].astype(str)+df_mdma['division'].astype(str)
    # #Convert to Dict
    # df_mdma_dict=dict(zip(df_mdma.key,df_mdma.forecast_delivery_time)) 
    # df_mdma_dict=dict(zip(df_mdma.key,df_mdma.planning_unit))    
    # #Get data from dict using map
    # df_mara_marc['forecast_delivery_time']=df_mara_marc['key'].map(df_mdma_dict)
    # df_mara_marc['planning_unit']=df_mara_marc['key'].map(df_mdma_dict)
    # print(df_mara_marc)
     #Delete dataframe not used

    ##############################
    #MARA MARC and  CEPC
    ##############################
    #Delete key
    del df_mara_marc['key'] 
    #Add  new key to DF mara_marc
    df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['ctrpr'].astype(str)
    #Add key to DF
    df_cepc['key']=df_cepc['year'].astype(str)+df_cepc['week'].astype(str)+df_cepc['profit_center'].astype(str)
     #Convert to Dict
    df_cepc_dict=dict(zip(df_cepc.key,df_cepc.district)) 
    #Get data from dict using map
    df_mara_marc['district']=df_mara_marc['key'].map(df_cepc_dict)
  
    #Delete dataframe not used

    ##############################
    #ZPP and  ST
    ##############################
    #Add key to DF
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)
    df_st['key']=df_st['year'].astype(str)+df_st['week'].astype(str)+df_st['material'].astype(str)

    #Convert to Dict
    df_st_dict=dict(zip(df_st.key,df_st.num_parcel))
    df_st_dict=dict(zip(df_st.key,df_st.delivery_qty))

    #Get data from dict using map
    df_zpp['num_parcel']=df_zpp['key'].map(df_st_dict)
    df_zpp['delivery_qty']=df_zpp['key'].map(df_st_dict)

    #Delete dataframe not used

    ##############################
    #ZPP and  MB52
    ##############################
    #Delete key
    del df_zpp['key'] 
    del df_mb52['key']
    #Add key to DF
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    df_mb52['key']=df_mb52['year'].astype(str)+df_mb52['week'].astype(str)+df_mb52['material'].astype(str)+df_mb52['division'].astype(str)
    #Convert to Dict
    df_mb52_dict=dict(zip(df_mb52.key,df_mb52.value_free_use))
    df_mb52_dict=dict(zip(df_mb52.key,df_mb52.descr_of_storage_loc))
    #Get data from dict using map
    df_zpp['value_free_use']=df_zpp['key'].map(df_mb52_dict)
    df_zpp['descr_of_storage_loc']=df_zpp['key'].map(df_mb52_dict)
     #Delete dataframe not used

    ##############################
    #ZPP and  ZMM
    ##############################
    #Add key to DF
    df_zmm['key']=df_zmm['year'].astype(str)+df_zmm['week'].astype(str)+df_zmm['material'].astype(str)+df_zmm['division'].astype(str)
    #Convert to Dict
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.validated_delivery_date))
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.confirmed_quantity))
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.purchasing_group))
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.vendor_name))
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.validated_delivery_date))
    df_zmm_dict=dict(zip(df_zmm.key,df_zmm.contractual_delivery_date))
    #Get data from dict using map
    df_zpp['validated_delivery_date']=df_zpp['key'].map(df_zmm_dict)
    df_zpp['confirmed_quantity']=df_zpp['key'].map(df_zmm_dict)
    df_zpp['purchasing_group']=df_zpp['key'].map(df_zmm_dict)
    df_zpp['vendor_name']=df_zpp['key'].map(df_zmm_dict)
    df_zpp['validated_delivery_date']=df_zpp['key'].map(df_zmm_dict)
    df_zpp['contractual_delivery_date']=df_zpp['key'].map(df_zmm_dict)
    #Delete dataframe not used
    ##############################
    #ZPP and  MARA MARC
    ##############################
    #Delete key 
    del df_mara_marc['key']
    #Add key to DF
    df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['material'].astype(str)+df_mara_marc['division'].astype(str)
    #Convert to Dict
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.tyar))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.mp))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.gac))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.a_s))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.typ))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.ctrpr))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.dpr))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.district))
    # df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.planning_unit))
    # df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.forecast_delivery_time))
    df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.purchasing_group))
    #Get data from dict using map
    df_zpp['tyar']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['mp']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['gac']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['a_s']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['typ']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['ctrpr']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['dpr']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['district']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['planning_unit']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['forecast_delivery_time']=df_zpp['key'].map(df_mara_marc_dict)
    df_zpp['purchasing_group']=df_zpp['key'].map(df_mara_marc_dict)
    del df_zpp['key']
    df_zpp['id']=df_zpp.index
    df_zpp=df_zpp.head(10)
    print(df_zpp)
    # df_zpp.to_csv(r'C:\Users\bibas\Downloads\zpp.csv',index=False)
    #Pagination
    #Convert  DataFrame to Dic
    records=df_zpp.to_dict(orient='records')
    print(records)
    #Paginator
    paginator=Paginator(records,5) # 30 is number of element in one page
    page = request.GET.get('page')
    records=paginator.get_page(page)
    #End Paginator
    #End Pagination


    return render(request,'app/overview.html',{'records':records})
def kpi(request):
    divisions={'FOU-2110':'2110','LAB-2000':'2000','LEC-2030':'2030','LIP-2020':'2020','COL-2010':'2010','HBG-2200':'2200','HER-2300':'2300','CAS-2400':'2400','BEL-2500':'2500','LAV-2600':'2600','QRO-2320':'2320'}
    return render(request,'app/kpi.html',{'divisions':divisions})






