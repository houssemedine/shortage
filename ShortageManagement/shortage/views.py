# Create your views here.
from io import StringIO
from unittest import result
from django.shortcuts import render
from django.shortcuts import redirect
from django.db.utils import OperationalError
from django.contrib import messages
import pandas as pd
import numpy as np
import psycopg2
from datetime import datetime
import pathlib
from shortage.forms import Myform,Form
from django.db.models import Q
from .decorators import allowed_users
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from administration.templates import administration
from django.contrib.auth.models import User

from shortage.models import *
#function to upload files
def upload(request):
    # Delete all data before upload
    MB52.objects.all().delete()
    SE16N_CEPC.objects.all().delete()
    SE16N_T001L.objects.all().delete()
    SE16N_T024.objects.all().delete()
    ZMM_CARNET_CDE_IS.objects.all().delete()
    Stock_transit.objects.all().delete()
    MDMA.objects.all().delete()
    ART_MARA_MARC.objects.all().delete()
    ZPP_MD_Stock.objects.all().delete()
    Z_SC_M_0002.objects.all().delete()
    Z_SC_P_0004.objects.all().delete()
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
            file_zscm=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\Z_SC_M_0002.xlsx')
            file_zscp=pathlib.Path(r'C:\Users\bibas\Downloads\Input SAP\Z_SC_P_00004.xlsx')
            # zpp_md_stock=[
            #     r"C:\Users\bibas\Downloads\Input SAP\2000_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2010_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2020_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2030_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2040_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2110_ZPP_MD_STOCK.xlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2200_ZPP_MD_STOCKxlsx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2300_ZPP_MD_STOCK.xslx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2400_ZPP_MD_STOCK.xslx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2500_ZPP_MD_STOCK.xslx"
            #     r"C:\Users\bibas\Downloads\Input SAP\2600_ZPP_MD_STOCK.xslx"
            # ]


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
                import_file_SE16N_T001L(conn,file_se16nt001l,year,week,uploded_by,uploded_at)
                import_file_MB52(conn,file_mb52,year,week,uploded_by,uploded_at)
                import_file_SE16N_CEPC(conn,file_se16ncepc,year,week,uploded_by,uploded_at)    
                import_file_SE16N_T024(conn,file_se16nt024,year,week,uploded_by,uploded_at)    
                import_file_ART_MARA_MARC(conn,file_art,year,week,uploded_by,uploded_at)
                import_file_ZMM_CARNET_CDE_IS(conn,file_zmm,year,week,uploded_by,uploded_at)
                import_file_Stock_transit(conn,file_st,year,week,uploded_by,uploded_at)
                import_file_MDMA(conn,file_md,year,week,uploded_by,uploded_at)
                import_Z_SC_P_0004(conn,file_zscp,year,week,uploded_by,uploded_at)
                import_Z_SC_M_0002(conn,file_zscm,year,week,uploded_by,uploded_at)
                for division,file in zpp_md_stock.items():
                    import_file_ZPP_MD_Stock(conn,division,file,year,week,uploded_by,uploded_at)
            else:
                messages.error(request, 'Files not found')
        except OperationalError:
            messages.error(request,'Data base not found')

#function for import file MB52
def import_file_MB52(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file,names=['material','division','store','store_level_deletion_indicator','unit','for_free_use','currency','value_free_use','transit_transfer','transit_transfer_value', 'in_quality_control','value_quality_control', 'non_free_stock','non_free_value', 'blocked','blocked_stock_value','returns','blocked_return_stock_value',]) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #Convert Division and Store to int and fill nan with 0
    df['division']=df['division'].fillna(0)
    df['division']=df['division'].astype(int)
    df['store']=df['store'].fillna(0)
    df['store']=df['store'].astype(int)
    #read t001L
    data_tl001l=SE16N_T001L.objects.values('year','week','descr_of_storage_loc','division','store')
    df_tl001l=pd.DataFrame(list(data_tl001l))
     #MB52 and T001L
    ##############################
    #Add Key to DF
    df['key']=df['year'].astype(str)+df['week'].astype(str)+df['division'].astype(str)+df['store'].astype(str)
    df_tl001l['key']=df_tl001l['year'].astype(str)+df_tl001l['week'].astype(str)+df_tl001l['division'].astype(str)+df_tl001l['store'].astype(str)
    # #Convert to Dict
    df_tl001l_dict=dict(zip(df_tl001l.key,df_tl001l.descr_of_storage_loc))
    # #Get data from dict using map
    df['descr_of_storage_loc']=df['key'].map(df_tl001l_dict)
    df.insert(4,'stock_type',"",True)
    df.loc[( df.descr_of_storage_loc.str.contains("PRINC")) | (df.descr_of_storage_loc.str.contains("MAIN"))  , "stock_type"] = "warehouse_stock"
    df.loc[( df.descr_of_storage_loc.str.contains("BDL") ) | (df.descr_of_storage_loc.str.contains("PROD")) | (df.descr_of_storage_loc.str.contains("PRD")) | (df.descr_of_storage_loc.str.contains("LS"))| (df.descr_of_storage_loc.str.contains("SEMI")) , "stock_type"] = "workshop_stock"
    df.loc[( df.descr_of_storage_loc.str.contains("PUSH") ) | (df.descr_of_storage_loc.str.contains("FTWZ")) , "stock_type"] = "stock_zpush"
    df.loc[( df.descr_of_storage_loc.str.contains("QUAL") ) | (df.descr_of_storage_loc.str.contains("QT")) | (df.descr_of_storage_loc.str.contains("QLt")) | (df.descr_of_storage_loc.str.contains("QLT")) , "stock_type"] = "stock_quality"
    df.loc[( df.descr_of_storage_loc.isna() ), "stock_type"] = "other_stocks"
    # Delete Key 
    del df['key'] 
    # print(df)
    df=df.groupby(['year','week','material','division','stock_type']).agg({'value_free_use':'sum'}).reset_index()

    print(df)
    # df.to_excel('mb52.xlsx')
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
            #    'uploaded_by',
            #    'uploaded_at',
               'material',
               'division',
               'stock_type',
            #    'store', 
            #    'store_level_deletion_indicator',
            #    'unit',
            #    'for_free_use',	
            #    'currency',
               'value_free_use',
            #    'transit_transfer',
            #    'transit_transfer_value', 	
            #    'in_quality_control',
            #    'value_quality_control', 	
            #    'non_free_stock',	
            #    'non_free_value', 
            #    'blocked',
            #    'blocked_stock_value',
            #    'returns',	
            #    'blocked_return_stock_value',
            #    'descr_of_storage_loc',
            
            ],
            null='',
            sep=','
        )
    con.commit()
 
#function for Import file SE16N_CEPC
def import_file_SE16N_CEPC(con,file,year,week,username,uploaded_at):
        #Read file
        df = pd.read_excel(file,index_col=False,names=['profit_center', 'valid_to', 'controlling_area',  'valid_from', 'created_on', 'created_by','field_name_of_CO_PA_characteristic', 'department', 'person_responsible_for_profit_center', 'user_responsible', 'currency', 'successor_profit_center', 'country_key',	'title', 'name1', 'name2', 'name3',	'name4', 'city', 'district', 'street', 'po_box','postal_code', 'p_o_box_costal_code', 'language_key', 'telebox_number', 'telephone1', 'telephone2', 'fax_number','teletex_number', 'telex_number', 'data_line', 'printer_name', 'hierarchy_area', 'company_code','joint_venture', 'recovery_indicator', 'equity_type', 'tax_jurisdiction', 'region', 'usage', 'application', 'procedure','logical_system', 'lock_indicator', 'prctr_formula_planning_template', 'segment', 'name', 'long_text',	'profit_center_short_text_for_matchcode',]) # to read file excel
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
    df = pd.read_excel(file,index_col=False,names=['division','store','descr_of_storage_loc', 'store_level_deletion_indicator','negative_inventory','fix_stk_theo','mrp_code','authorization_check','stor_resource','management_missing_units', 'partner_store','sales_organization', 'distribution_channel','shipping_point_receiving_pt', 'vendor','customer','business_system_of_mes','inventory_management_type','license_number','in_transit_assignment','tank_assgn']) # to read file excel
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
    df = pd.read_excel(file,names=['purchasing_group', 'description_p_group', 'tel_no_purch_group',  'output_device', 'fax_number','telephone', 'extension', 'e_mail_address', 'user_name' ]) # to read file excel
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
    df = pd.read_excel(file,names=['request_no','division','store','purchase_document','poste1','due_date','vendor','vendor_name','material', 'designation_add_material','name','transmission_info','validated_by','priority', 'quantity','quantity_to_receive','date_of_purchase','desired_date','original_delivery_date','contractual_delivery_date', 'validated_delivery_date','confirmed_quantity','comment','expected_stock_week_w','expected_stock_week_w_1','expected_stock_week_w_2','expected_stock_week_w_3','expected_stock_week_w_4','expected_stock_week_w_5','expected_stock_week_w_6','expected_stock_week_w_7','expected_stock_week_w_8','expected_stock_week_w_9','expected_stock_week_w_10','expected_stock_week_w_11','expected_stock_week_w_12','confirmation','estimated_delivery_time','comment_vendor','element_otp','business_document','poste2','need_number','net_price','currency','price_basis','price_unit','net_order_value','purchasing_document_type','exception_message_number','exception_message','purchasing_group']) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #Convert Division and Store to int and fill nan with 0
    # df['Division']=df['Division'].fillna(0)
    # df['Division']=df['Division'].astype(int)
    df['store']=df['store'].fillna(0)
    df['store']=df['store'].astype(int)
     
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
    df = pd.read_excel(file,names=['material','plan_date','mrp_element','data_for_planning_element','action_message','Input_need','available_quantity','reorder_date','vendor','customer']) # to read file excel
    df.insert(0,'division',division,True)
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    df.insert(2,'week_number',df['plan_date'].dt.isocalendar().week,True) #Week Number based on plan date
    df.insert(3,'year_number',df['plan_date'].dt.isocalendar().year,True) #Year Number based on plan date
    df.insert(4,'year_week',df['year_number'].astype(str)+'_'+df['week_number'].astype(str))
    df.insert(5,'uploaded_by',username,True)
    df.insert(6,'uploaded_at',uploaded_at,True)
    #############################
    #ZPP and MRP ELEMENT 
    ##############################
    data_mrp_element=Mrp_element.undeleted_objects.values('fr','en','take_into_account')
    if data_mrp_element:
        df_mrp_element=pd.DataFrame(list(data_mrp_element))
        df_mrp_element_dict_fr=dict(zip(df_mrp_element.fr,df_mrp_element.take_into_account))
        df['take_into_account_fr']=df['mrp_element'].map(df_mrp_element_dict_fr)
        df_mrp_element_dict_en=dict(zip(df_mrp_element.en,df_mrp_element.take_into_account))
        df['take_into_account_en']=df['mrp_element'].map(df_mrp_element_dict_en)
        df=df[(df['take_into_account_en'] =='Y') |  (df['take_into_account_fr'] =='Y')]
        del df['take_into_account_en'] 
        del df['take_into_account_fr'] 
        del df['mrp_element'] 
        del df['data_for_planning_element'] 
        del df['action_message'] 
        del df['available_quantity'] 
        del df['reorder_date'] 
        del df['vendor']
        del df['customer']
        del df['week_number']
        del df['year_number']

    # df=df.groupby(['year','week','material','division']).agg({'Input_need': 'sum','available_quantity': 'sum'}).reset_index()

    #Get History data for need past calculte 
    # data_history=ZPP_MD_Stock.objects.values('material','division','Input_need').exclude(week=week)
    # if data_history:
    #     df_history=pd.DataFrame(list(data_history))
    #     df_history=df_history.groupby(['material','division']).agg({'Input_need':'sum'}).reset_index()
    #     df_history['key']=df_history['material'].astype(str)+df_history['division'].astype(str)
    #     df_history_dict=dict(zip(df_history.key,df_history.Input_need))
    #     df['key']=df['material'].astype(str)+df['division'].astype(str)
    #     df['need_past']=df['key'].map(df_history_dict)
    #     #Delete Key 
    #     del df['key']
    # else:
    #     df['need_past']=0
    #Cconvert to csv 
    print(df)

    df=df.to_csv(index=False,sep='|',header=None)  
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
                'year_week',
                'uploaded_by',
                'uploaded_at',
                'division',
                'material',
                'plan_date',	
                'Input_need'
            ],
            null='',
            sep='|'
        )
    con.commit() 

#function for Import file 
def import_file_Stock_transit(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file,names=['pExp','division','transfer_code', 'poscde','tLvr','actual_sm','delivery','item','num_picking_UUID', 'num_parcel','material', 'delivery_qty','uq','qty_delivered','qty_received','not_received','customer_order', 'of_art_description','msn',	'appro_Special','comment','n_of','article_of' ]) # to read file excel
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
               'division',
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
    df = pd.read_excel(file,names=['material','material_designation','text_material', 'market_group','division','ctrpr','typ_app','a_s','tcy','dfi', 'dpr','horiz', 'mp','r', 'tyar','nai','i_c','aappr_def','mgApp','mag','tl','fixed_batch','uq1','security_stock', 'uq2','tre','gest','di','scrap','gac','profile', 'prpiat','created_by', 'language','created_on', 'gcha','gs','comparison_mode_of_the_requirements','int_adjustment_upstream','int_adjustment_downstream','size_l_min', 'uq3','rounded_value','uq4','lot_size_mx','uq5','maximum_stock','uq6', 'edge','typ', 'time_limit1','time_limit2', 'recipient_ctrl','material_filled','dv',	'gml','grpi','abc','uq7','wbs_element','grpa','control_code','product_hierarchy', 'gross_weight','unp1', 'net_weight','unp2', 'no_ccr','ccr_lot_size','uq8']) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    #read CEPC
    data_cepc=SE16N_CEPC.objects.values('year','week','district','profit_center','profit_center_short_text_for_matchcode')
    df_cepc=pd.DataFrame(list(data_cepc))

    ##############################
    #MARA MARC and  CEPC
    ##############################
    #Add  new key to DF mara_marc
    df['key']=df['year'].astype(str)+df['week'].astype(str)+df['ctrpr'].astype(str)
    #Add key to DF
    df_cepc['key']=df_cepc['year'].astype(str)+df_cepc['week'].astype(str)+df_cepc['profit_center'].astype(str)
    #Convert to Dict
    df_cepc_dict_district=dict(zip(df_cepc.key,df_cepc.district)) 
    df_cepc_dict_profit_center_short_text_for_matchcode=dict(zip(df_cepc.key,df_cepc.profit_center_short_text_for_matchcode)) 

    #Get data from dict using map
    df['district']=df['key'].map(df_cepc_dict_district)
    df.insert(4,'scope_allocation',"Not Found",True)
    df['district']=df['district'].fillna("Not found")
    
    df.loc[( df.district.str.contains("SERIE", na=False)) , "scope_allocation"] = "SERIAL"
    df.loc[( df.district.str.contains("HORS SERIE")) , "scope_allocation"] = "NO AIRCRAFT"
    df.loc[( df.district.str.contains("SPATIAL")) , "scope_allocation"] = "SPACE"
    df['profit_center_designation']=df['key'].map(df_cepc_dict_profit_center_short_text_for_matchcode)
    #Delete key 
    del df['key']
    #read T024
    data_t024=SE16N_T024.objects.values('year','week','purchasing_group','description_p_group')
    df_t024=pd.DataFrame(list(data_t024))
    #############################
    #MARA MARC and T024
    #############################
    #Add key to DF
    df['key']=df['year'].astype(str)+df['week'].astype(str)+df['gac'].astype(str)
    df_t024['key']=df_t024['year'].astype(str)+df_t024['week'].astype(str)+df_t024['purchasing_group'].astype(str)
    #Convert to Dict
    df_t024_dict=dict(zip(df_t024.key,df_t024.description_p_group))    
    # #Get data from dict using map
    df['purchasing_group_designation']=df['key'].map(df_t024_dict)
    #Delete key 
    del df['key']
    # df=df.head(20)
    print(df)
    # df.to_excel('mara_marc.xlsx')
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
               'scope_allocation',
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
               'district',
               'profit_center_designation',
               'purchasing_group_designation',
            ],
            null='',
            sep=';'
        )
    con.commit()

#function for import file MDMA
def import_file_MDMA(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file,names=['material','planning_unit','division','planning_profile','planning_type','manager','planning_group','order_point','planning_rate','fixed_planning_horizon','lot_size_calculation_key','rounding_profile','rounding_value','minimum_lot_size','maximum_lot_size','maximum_stock','cycle','rejects_ss_ens','special_supply','production_store','store_for_external_supply','planning_calendar','safety_stock','coverage_profile','safety_stock_actual_stock','fixed_lot_size','fixed_lot_costs','storage_cost_code','service_rate','forecast_profile','ref_cons_val','un_plan_cons','au','multiplier','suppr_indicator','prof_per_sec','dependent_needs_planner','reset_auto','management_status','correction_pow','safety_time','for_apo','forecast_delivery_time','take_into_account_the_expected_delivery_time'])# to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    print(df)
    df=df.to_csv(index=False,header=None) #To convert to csv
    # print(df)
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

def import_Z_SC_P_0004(con,file,year,week,username,uploaded_at):
    #Read file
    df = pd.read_excel(file,names=['notice','vendor','supplier_account_number','created_on','created_by','system_status','division','gac','purchase_document','poste','material','num_material','reference','date','updated_by','updated_on']) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    print(df)
    df=df.to_csv(index=False,sep=';',header=None) #To convert to csv
    # print(df)
    zscp=StringIO()
    zscp.write(df)
    zscp.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zscp,
            table="shortage_z_sc_p_0004",
            columns=[
                'year',
                'week',
                'uploaded_by',
                'uploaded_at',
                'notice',
                'vendor',
                'supplier_account_number',
                'created_on',
                'created_by',
                'system_status',
                'division',
                'gac',
                'purchase_document',
                'poste',
                'material',
                'num_material',
                'reference',
                'date',
                'updated_on',
                'updated_by',
                ],
            null='',
            sep=';'
        )
    con.commit()

def import_Z_SC_M_0002(con,file,year,week,username,uploaded_at):
       #Read file
    df = pd.read_excel(file,names=['material','num_material','division','orga','tyar','sa','a_s','fra','vendor','name1','contract','post','purchase_info','uq1','gest1','val_arrondie','uq2','orig','gac1','tps_de_recep','dpl','uac1','px_busgt_cours','dev1','pbudg_prec','dev2','futur_budget_price','dev3','par1','cival','por','sgf','num_material_fourn','gac2','dpr1','net_price','dev4','par2','inctm','incpterms','qte_standard','uac2','qte_min','uac3','name2','uac4','corr','post_type','target_qte','uac5','gac3','price_net','dev5','dev6','par3','i','num_material_fourn','tre','tps_fab_ext','inctm_contract','inctm_contract2','gac4','dev7','inctm2','incoterms2','grpi1','abc','planning_unit','gest2','a_s2','dpr2','grpi2','apsc','num_tarif_dnr',]) # to read file excel
    #insert 2 column year, week
    df.insert(0,'year',year,True)
    df.insert(1,'week',week,True)
    #insert 2 column created by, created at
    df.insert(2,'uploaded_by',username,True)
    df.insert(3,'uploaded_at',uploaded_at,True)
    print(df)
    df=df.to_csv(index=False,sep=';',header=None) #To convert to csv
    # print(df)
    zscm=StringIO()
    zscm.write(df)
    zscm.seek(0)
    with con.cursor() as curs:
        curs.copy_from(
            file=zscm,
            table="shortage_z_sc_m_0002",
            columns=[
                'year',
                'week',
                'uploaded_by',
                'uploaded_at',
                'material',
                'num_material',
                'division',
                'orga',
                'tyar',
                'sa',
                'a_s1',
                'fra',
                'vendor',
                'name1',
                'contract',
                'post',
                'purchase_info',
                'uq1',
                'gest1',
                'val_arrondie',
                'uq2',
                'orig',
                'gac1',
                'tps_de_recep',
                'dpl',
                'uac1',
                'px_busgt_cours',
                'dev1',
                'pbudg_prec',
                'dev2',
                'futur_budget_price',
                'dev3',
                'par1',
                'cival',
                'por',
                'sgf',
                'num_material_fourn1',
                'gac2',
                'dpr1',
                'net_price',
                'dev4',
                'par2',
                'inctm',
                'incpterms',
                'qte_standard',
                'uac2',
                'qte_min',
                'uac3',
                'name2',
                'uac4',
                'corr',
                'post_type',
                'target_qte',
                'uac5',
                'gac3',
                'price_net',
                'dev5',
                'dev6',
                'par3',
                'i',
                'num_material_fourn2',
                'tre',
                'tps_fab_ext',
                'inctm_contract',
                'inctm_contract2',
                'gac4',
                'dev7',
                'inctm2',
                'incoterms2',
                'grpi1',
                'abc',
                'planning_unit',
                'gest2',
                'a_s2',
                'dpr2',
                'grpi2',
                'apsc',
                'num_tarif_dnr',
                ],
            null='',
            sep=';'
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
    return render(request,r'shortage\core.html',{'data':data,'filter':filter})

@allowed_users(allowed_roles=['users','administrators'])
def create_core(request):#create new core
    if  (request.method == 'POST') :
        material=request.POST['material']
        division=request.POST['division']
        data=Core.undeleted_objects.all().filter(material=material,division=division).exclude(status='Close')
        print(data.first())
        if data:
            messages.warning(request,'Core is already exist !')
            # return render(request,'shortage/core_history.html',{'pk':data.first().id,'data':data})
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

    return render(request,'shortage\create_core.html',{'myform' : Myform})

@allowed_users(allowed_roles=['administrators','users'])
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
            # return render(request,'shortage/core_history.html',{'pk':data.first().id,'data':data})
            return core_history(request,data.first().id)
        else:
            if myform.is_valid():
                myform.save()
                messages.success(request,"Core updated successfully!")
                return redirect('core')
            else:
                messages.error(request, 'Invalid form submission.') 
    return render(request,'shortage/updateForm.html',{'core' : core,'myform' : myform})

@allowed_users(allowed_roles=['administrators'])
def delete_core(request,pk): #function soft-delete
    core=Core.objects.get(id=pk)
    core.deleted=True
    core.deleted_on=datetime.now()
    core.deleted_by=1
    core.save()
    return redirect('core')

def core_history(request,pk):
    username='bibas'
    role=User.objects.all().filter(username=username).values_list('groups__name')
    data=CoreHistory.objects.all().filter(core_id=pk).order_by('-id')
    core=Core.objects.filter(id=pk).all()
    current_status=core.values('status').reverse()[0]
    return render(request,'shortage/core_history.html',{'form':Form,'pk':pk,'data':data,'core':core,'role':role,'current_status':current_status})


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
    return redirect('core')

#overview
def overview(request):
    # year=datetime.now().isocalendar()[0]
    # week=datetime.now().isocalendar()[1]
    year=2022
    week=9

    #Call all files
    data_zpp=ZPP_MD_Stock.objects.values('year','week','year_week','material','Input_need','division')
    data_mb52=MB52.objects.values('year','week','value_free_use','material','division','stock_type')
    data_mdma=MDMA.objects.values('year','week','forecast_delivery_time','planning_unit','material','division')
    data_mara_marc=ART_MARA_MARC.objects.values('year','week','tyar','mp','gac','a_s','typ','ctrpr','dpr','material','division','scope_allocation','district','profit_center_designation','purchasing_group_designation')
    data_core=Core.undeleted_objects.values('id','material','division','status','created_by')
    data_zmm=ZMM_CARNET_CDE_IS.objects.values('week','year','material','division','purchase_document','purchasing_group','validated_delivery_date','confirmed_quantity','vendor_name','poste1')
    data_st=Stock_transit.objects.values('year','week','num_parcel','delivery_qty','material','division')
    #Convert to dataFrame
    df_zpp=pd.DataFrame(list(data_zpp))
    df_st=pd.DataFrame(list(data_st))
    df_mb52=pd.DataFrame(list(data_mb52))
    df_core=pd.DataFrame(list(data_core))
    df_zmm=pd.DataFrame(list(data_zmm))
    df_mara_marc=pd.DataFrame(list(data_mara_marc))
    df_mdma=pd.DataFrame(list(data_mdma))
    df_zpp['Input_need']=df_zpp['Input_need'].astype(np.float64)
    ##############################
    # Zpp Pivot table 
    ##############################

    df_zpp=df_zpp.pivot_table(index=['year','week','material','division'],columns='year_week',values='Input_need', aggfunc='sum').reset_index()


    ##############################
    # ZPP and  ST
    ##############################
    # #Add key to DF
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    df_st['key']=df_st['year'].astype(str)+df_st['week'].astype(str)+df_st['material'].astype(str)+df_st['division'].astype(str)
    # #Convert to Dict
    df_st_dict_num_parcel=dict(zip(df_st.key,df_st.num_parcel))
    df_st_dict_delivery_qty=dict(zip(df_st.key,df_st.delivery_qty))
    # #Get data from dict using map
    df_zpp['num_parcel']=df_zpp['key'].map(df_st_dict_num_parcel)
    df_zpp['delivery_qty']=df_zpp['key'].map(df_st_dict_delivery_qty)
    #Delete Key 
    del df_zpp['key']
    #############################
    #ZPP and MB52
    # ##############################
    df_mb52['key']=df_mb52['year'].astype(str)+df_mb52['week'].astype(str)+df_mb52['material'].astype(str)+df_mb52['division'].astype(str)
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    # #Convert to dict
    # df_mb52_dict_stock_type=dict(zip(df_mb52.key,df_mb52.stock_type))
    # df_zpp['stock_type']=df_zpp['key'].map(df_mb52_dict_stock_type)
    df_mb52['stock_type']=df_mb52['stock_type'].fillna('not_defined')
    # df_mb52=df_mb52.pivot(index=['year','week','material','division'],columns=['stock_type'],values='value_free_use').reset_index()
    df_mb52=df_mb52.pivot_table(index=['year','week','material','division'],columns='stock_type',values='value_free_use', aggfunc='sum').reset_index()
    df_mb52['key']=df_mb52['year'].astype(str)+df_mb52['week'].astype(str)+df_mb52['material'].astype(str)+df_mb52['division'].astype(str)
    df_mb52_dict_other_stocks=dict(zip(df_mb52.key,df_mb52.other_stocks))
    df_mb52_dict_stock_quality=dict(zip(df_mb52.key,df_mb52.stock_quality))
    df_mb52_dict_stock_zpush=dict(zip(df_mb52.key,df_mb52.stock_zpush))
    df_mb52_dict_warehouse_stock=dict(zip(df_mb52.key,df_mb52.warehouse_stock))
    df_mb52_dict_workshop_stock=dict(zip(df_mb52.key,df_mb52.workshop_stock))

    df_zpp['other_stocks']=df_zpp['key'].map(df_mb52_dict_other_stocks)
    df_zpp['stock_quality']=df_zpp['key'].map(df_mb52_dict_stock_quality)
    df_zpp['stock_zpush']=df_zpp['key'].map(df_mb52_dict_stock_zpush)
    df_zpp['warehouse_stock']=df_zpp['key'].map(df_mb52_dict_warehouse_stock)
    df_zpp['workshop_stock']=df_zpp['key'].map(df_mb52_dict_workshop_stock)
    ##################################################
    # Calculate Needs in the past of the current week
    ##################################################
    #Get index for current week
    # index_current_week=df_zpp.columns.get_loc(str(year)+'_'+str(week))
    index_current_week=df_zpp.columns.get_loc(str(year)+'_'+str(week)) #temporarily, to delete 
    index_first_col=df_zpp.columns.get_loc('division')
    df_zpp['needs_in_past'+'_'+str(year)+'_'+str(week)]=df_zpp.iloc[:,index_first_col+1:index_current_week].sum(axis=1)
    ####################################
    # Calculate Stock of the current week
    ####################################
    col_list_to_sum=[str(year)+'_'+str(week),'delivery_qty','needs_in_past'+'_'+str(year)+'_'+str(week),'warehouse_stock','workshop_stock','stock_zpush','other_stocks']
    df_zpp['stock'+'_'+str(year)+'_'+str(week)]=df_zpp[col_list_to_sum].sum(axis=1)
    #Get Nbre of futur week
    futur_week=5
    #Calcul Stock of futur week
    list_sum=['stock'+'_'+str(year)+'_'+str(week),str(year)+'_'+str(week+1),'delivery_qty']
    df_zpp['stock'+'_'+str(year)+'_'+str(week+1)]=df_zpp[list_sum].sum(axis=1)
    i=2
    while i < futur_week+1:
        df_zpp.insert(0,'stock'+'_'+str(year)+'_'+str(week+i),'',True)
        col_list_for_sum=['stock'+'_'+str(year)+'_'+str(week+i-1),str(year)+'_'+str(week+i),'delivery_qty']
        df_zpp['stock'+'_'+str(year)+'_'+str(week+i)]=df_zpp[col_list_for_sum].sum(axis=1)
        i += 1
    # Delete Key 
    del df_mb52['key']
    del df_zpp['key']
    ##############################
    #ZPP and CORE
    ##############################
    #Add  new key to DF  Core
    df_core['key']=df_core['material'].astype(str)+df_core['division'].astype(str)
    df_zpp['key']=df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    # #Convert to Dict
    df_core_dict_id=dict(zip(df_core.key,df_core.id))
    df_core_dict_status=dict(zip(df_core.key,df_core.status))
    df_zpp['id_core']=df_zpp['key'].map(df_core_dict_id)
    df_zpp['status_core']=df_zpp['key'].map(df_core_dict_status)
    del df_zpp['key']
    ##############################
    #ZPP and ZMM 
    ##############################
    #Add key to DF
    df_zmm['key']=df_zmm['year'].astype(str)+df_zmm['week'].astype(str)+df_zmm['material'].astype(str)+df_zmm['division'].astype(str)
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    df_zmm_dict_purchase_document=dict(zip(df_zmm.key,df_zmm.purchase_document))
    df_zmm_dict_purchasing_group=dict(zip(df_zmm.key,df_zmm.purchasing_group))
    df_zmm_dict_validated_delivery_date=dict(zip(df_zmm.key,df_zmm.validated_delivery_date))
    df_zmm_dict_confirmed_quantity=dict(zip(df_zmm.key,df_zmm.confirmed_quantity))
    df_zmm_dict_vendor_name=dict(zip(df_zmm.key,df_zmm.vendor_name))
    df_zmm_dict_poste1=dict(zip(df_zmm.key,df_zmm.poste1))
    df_zpp['purchase_document']=df_zpp['key'].map(df_zmm_dict_purchase_document)
    df_zpp['poste1']=df_zpp['key'].map(df_zmm_dict_poste1)
    df_zpp['ongoing_po']=df_zpp['purchase_document'].astype(str)+'-'+df_zpp['poste1'].astype(str)
    del df_zpp['purchase_document']
    del df_zpp['poste1']
    # df_zpp['confirmed_delivery_date']=df_zpp['key'].map(df_zmm_dict_validated_delivery_date)
    df_zpp['quantity_to_receive']=df_zpp['key'].map(df_zmm_dict_confirmed_quantity)
    df_zpp['procurement_agent']=df_zpp['key'].map(df_zmm_dict_purchasing_group)
    df_zpp['po_supplier']=df_zpp['key'].map(df_zmm_dict_vendor_name)
    # df_zpp.to_excel('zpp_last_one.xlsx')
    #MARA MARC and  MDMA
    ##############################
    #Add  new key to DF mara_marc
    df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['material'].astype(str)+df_mara_marc['division'].astype(str)
    #Add key to DF
    df_mdma['key']=df_mdma['year'].astype(str)+df_mdma['week'].astype(str)+df_mdma['material'].astype(str)+df_mdma['division'].astype(str)
    #Convert to Dict
    # df_mara_marc_dict=dict(zip(df_mara_marc.key, df_mara_marc.a_s))
    df_mdma_dict_planning_unit=dict(zip(df_mdma.key,df_mdma.planning_unit)) 

    df_mara_marc['planning_unit']=df_mara_marc['key'].map(df_mdma_dict_planning_unit)
    df_mara_marc.a_s=df_mara_marc.a_s.fillna(0)
    df_mara_marc.a_s=df_mara_marc.a_s.astype(str)
    df_mara_marc['mrp_area']=np.where(df_mara_marc.a_s.str.startswith('5'),df_mara_marc['planning_unit'],'')
     # #ZPP and  MARA MARC
    # ##############################
    # #Delete key 
    del df_mara_marc['key']
    # #Add key to DF
    df_mara_marc['key']=df_mara_marc['year'].astype(str)+df_mara_marc['week'].astype(str)+df_mara_marc['material'].astype(str)+df_mara_marc['division'].astype(str)
    df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    # #Convert to Dict
    df_mara_marc_dict_tyar=dict(zip(df_mara_marc.key,df_mara_marc.tyar))
    df_mara_marc_dict_mp=dict(zip(df_mara_marc.key,df_mara_marc.mp))
    df_mara_marc_dict_profit_center_designation=dict(zip(df_mara_marc.key,df_mara_marc.profit_center_designation))
    df_mara_marc_dict_a_s=dict(zip(df_mara_marc.key,df_mara_marc.a_s))
    df_mara_marc_dict_typ=dict(zip(df_mara_marc.key,df_mara_marc.typ))
    df_mara_marc_dict_purchasing_group_designation=dict(zip(df_mara_marc.key,df_mara_marc.purchasing_group_designation))
    df_mara_marc_dict_mrp_area=dict(zip(df_mara_marc.key,df_mara_marc.mrp_area))
    df_mara_marc_dict_scope_allocation=dict(zip(df_mara_marc.key,df_mara_marc.scope_allocation))
    df_mara_marc_dict_dpr=dict(zip(df_mara_marc.key,df_mara_marc.dpr))
    # df_mara_marc_dict=dict(zip(df_mara_marc.key,df_mara_marc.forecast_delivery_time))
    # df_mara_marc_dict_purchasing_group=dict(zip(df_mara_marc.key,df_mara_marc.purchasing_group))
    # # #Get data from dict using map
    df_zpp['tyar']=df_zpp['key'].map(df_mara_marc_dict_tyar)
    df_zpp['mp']=df_zpp['key'].map(df_mara_marc_dict_mp)
    df_zpp['profit_center_designation']=df_zpp['key'].map(df_mara_marc_dict_profit_center_designation)
    df_zpp['a_s']=df_zpp['key'].map(df_mara_marc_dict_a_s)
    df_zpp['typ']=df_zpp['key'].map(df_mara_marc_dict_typ)
    df_zpp['purchasing_group_designation']=df_zpp['key'].map(df_mara_marc_dict_purchasing_group_designation)
    df_zpp['mrp_area']=df_zpp['key'].map(df_mara_marc_dict_mrp_area)
    df_zpp['scope_allocation']=df_zpp['key'].map(df_mara_marc_dict_scope_allocation)
    df_zpp['dpr']=df_zpp['key'].map(df_mara_marc_dict_dpr)
    # df_zpp['forecast_delivery_time']=df_zpp['key'].map(df_mara_marc_dict)
    # df_zpp['purchasing_group']=df_zpp['key'].map(df_mara_marc_dict_purchasing_group)
    # del df_zpp['key']
    df_zpp['id']=df_zpp.index
    # df_mb52.to_excel('mb52.xlsx')
    # df_mb52.to_excel('mb52.xlsx' )

    ##############################
    #ZPP and  MB52
    ##############################
    # #Delete key
    # del df_zpp['key'] 
    # del df_mb52['key']
    # #Add key to DF
    # df_zpp['key']=df_zpp['year'].astype(str)+df_zpp['week'].astype(str)+df_zpp['material'].astype(str)+df_zpp['division'].astype(str)
    # df_mb52['key']=df_mb52['year'].astype(str)+df_mb52['week'].astype(str)+df_mb52['material'].astype(str)+df_mb52['division'].astype(str)
    # #Convert to Dict
    # df_mb52_dict=dict(zip(df_mb52.key,df_mb52.value_free_use))
    # df_mb52_dict=dict(zip(df_mb52.key,df_mb52.descr_of_storage_loc))
    # #Get data from dict using map
    # df_zpp['value_free_use']=df_zpp['key'].map(df_mb52_dict)
    # df_zpp['descr_of_storage_loc']=df_zpp['key'].map(df_mb52_dict)
    ##############################
    #calcul missing status
    ##############################
    list_futur_week=list(range(week+1,week+futur_week))
    df_zpp.insert(0,'missing_status',None,True)
    for first_week, successive_week in zip(list_futur_week, list_futur_week[1:]):
        df_zpp['missing_status']=np.where((df_zpp.missing_status.isna()) & (df_zpp['stock'+'_'+str(year)+'_'+str(first_week)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(successive_week)] < 0),'Shortage',df_zpp['missing_status'])
    #Immidiate Shortage
    df_zpp['missing_status']=np.where((df_zpp['stock'+'_'+str(year)+'_'+str(week+1)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(week+2)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(week+3)] < 0),'Immidiate Shortage',df_zpp['missing_status'])
    df_zpp['missing_status']=np.where((df_zpp['stock'+'_'+str(year)+'_'+str(week+1)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(week+2)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(week+3)] < 0) & (df_zpp['stock'+'_'+str(year)+'_'+str(week+4)] < 0),'Heavy shortage',df_zpp['missing_status'])
    df_zpp['missing_status']=df_zpp['missing_status'].fillna('Covred')
    ##############################
    # df_zpp.to_excel('zpp.xlsx')
    overview.df_zpp=df_zpp
    #Pagination
    #Convert  DataFrame to Dic
    records=df_zpp.to_dict(orient='records')
    # print(records)
    #Paginator
    paginator=Paginator(records,30) # 30 is number of element in one page
    page = request.GET.get('page')
    records=paginator.get_page(page)
    #End Paginator
    #End Pagination


    return render(request,'shortage/overview.html',{'records':records})
def kpi(request):
    overview(request)
    #################
    # KPIs
    #################
    # status_week=overview.df_zpp.groupby("missing_status")["missing_status"].count()
    status_week=overview.df_zpp.groupby("missing_status").agg({'id':'count'}).reset_index()
    status_week_per_division=overview.df_zpp.groupby(["division","missing_status"]).agg({'id':'count'}).reset_index()
    divisions_filter={'FOU-2110':'2110','LAB-2000':'2000','LEC-2030':'2030','LIP-2020':'2020','COL-2010':'2010','HBG-2200':'2200','HER-2300':'2300','CAS-2400':'2400','BEL-2500':'2500','LAV-2600':'2600','QRO-2320':'2320'}
    divisions={'2110','2000','2030','2020','2010','2200','2300','2400','2500','2600','2320'}
    missing_status=['Shortage','Immidiate Shortage','Covred']
    return render(request,'shortage/kpi.html',{'divisions_filter':divisions_filter,'divisions':divisions,'status_week':status_week,'status_week_per_division':status_week_per_division,'missing_status':missing_status})






