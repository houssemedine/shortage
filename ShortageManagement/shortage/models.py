from datetime import  datetime
from django.db import models

# Create your models here.

class MB52(models.Model): #Model For File  MB52
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    # uploaded_by=models.IntegerField(null=True)
    # uploaded_at=models.DateTimeField(null=True)
    stock_type=models.CharField(max_length=100,null=True) #add calculate column at upload 
    material = models.CharField(max_length=30,null=True) #Numéro d'article	
    division = models.IntegerField(null=True) #Division
    # store = models.IntegerField(null=True) #Magasin
    # store_level_deletion_indicator =models.CharField(max_length=15,null=True) #Tém.suppr.:niv. mag	
    # unit=models.CharField(max_length=5,null=True) #Unité de qté base
    # for_free_use= models.FloatField(null=True) #A utilisation libre	
    # currency=models.CharField(max_length=5,null=True) #Devise	
    value_free_use=models.FloatField(null=True)#Val. utilis. libre
    # transit_transfer=models.FloatField(null=True) #Transit et transfert
    # transit_transfer_value = models.FloatField(null=True) #Val. en Trnst&Tsft	
    # in_quality_control = models.FloatField(null=True) #En contrôle qualité	
    # value_quality_control = models.FloatField(null=True) #Val. ds ctrl.qual.	
    # non_free_stock=models.FloatField(null=True) #Stock non libre	
    # non_free_value =models.FloatField(null=True) #Valeur non libre
    # blocked=models.FloatField(null=True) #Bloqué	
    # blocked_stock_value=models.FloatField(null=True) #Val. stock bloqué	
    # returns=models.FloatField(null=True) #Retours	
    # blocked_return_stock_value=models.FloatField(null=True) #Val.stk ret.bloq.  
    # descr_of_storage_loc = models.CharField(max_length=100,null=True) #add column from t001l



class SE16N_CEPC(models.Model): #Model For File  SE16N_CEPC
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    profit_center = models.CharField(max_length=30,null=True) #Centre de profit
    valid_to = models.DateTimeField(null=True) #Fin de validité
    controlling_area = models.CharField(max_length=30,null=True) #Périmètre analytique
    valid_from =models.DateTimeField(null=True) #Début de validité  
    created_on=models.DateTimeField(null=True) #Saisi le  
    created_by= models.CharField(max_length=30,null=True) #Saisi par      
    field_name_of_CO_PA_characteristic=models.CharField(max_length=30,null=True) #Nom de zone de caractér. ds CO-PA  
    department=models.CharField(max_length=30,null=True) #Département  
    person_responsible_for_profit_center=models.CharField(max_length=30,null=True) #Responsable centre de profit
    user_responsible=models.CharField(max_length=30,null=True) #Utilisateur responsable
    currency = models.CharField(null=True , max_length=10) #Devise    
    successor_profit_center = models.CharField(max_length=30,null=True) #Centre de profit suivant    
    country_key = models.CharField(max_length=10,null=True) #Clé de pays
    title = models.CharField(max_length=30,null=True) #Titre de civilité  
    name1 = models.CharField(max_length=30,null=True)  #Nom 1  
    name2 = models.CharField(max_length=30,null=True)  #Nom 2  
    name3 = models.CharField(max_length=30,null=True)  #Nom 3
    name4 = models.CharField(max_length=30,null=True)  #Nom 4  
    city = models.CharField(max_length=10,null=True)  #ville  
    district = models.CharField(max_length=30,null=True)  #Arrondissement        
    street = models.CharField(max_length=30,null=True)  #Rue    
    po_box = models.CharField(max_length=10,null=True)  #Boîte postale
    postal_code = models.CharField(max_length=30,null=True) #Code postal
    p_o_box_costal_code = models.CharField(max_length=30,null=True) #CdP-Boîte postale  
    language_key = models.CharField(max_length=10,null=True) #Code langue    
    telebox_number = models.CharField(max_length=30,null=True) #Nº boîte électroniq.    
    telephone1 = models.CharField(max_length=30,null=True) #Téléphone 1
    telephone2 = models.CharField(max_length=30,null=True) #Téléphone 2
    fax_number = models.CharField(max_length=30,null=True) #Numéro de télécopie
    teletex_number = models.CharField(max_length=30,null=True) #Numéro de télétex  
    telex_number = models.CharField(max_length=30,null=True) #Numéro de télex
    data_line = models.CharField(max_length=30,null=True) #Ligne transmission  
    printer_name = models.CharField(max_length=30,null=True) #Nom imprimante  
    hierarchy_area = models.CharField(max_length=30,null=True) #Dom. hiérarchie
    company_code = models.CharField(max_length=30,null=True) #Société
    joint_venture = models.CharField(max_length=30,null=True) #Joint venture  
    recovery_indicator = models.CharField(max_length=30,null=True) #Catégorie de coûts  
    equity_type = models.CharField(max_length=30,null=True) #Classe participation
    tax_jurisdiction = models.CharField(max_length=30,null=True) #Juridiction fiscale
    region = models.CharField(max_length=30,null=True)  # Région    
    usage = models.CharField(max_length=30,null=True) #Emploi  
    application = models.CharField(max_length=30,null=True) #Application
    procedure = models.CharField(max_length=30,null=True) #schéma  
    logical_system = models.CharField(max_length=30,null=True) #Système logique
    lock_indicator = models.CharField(max_length=30,null=True) #code de blocage
    prctr_formula_planning_template = models.CharField(max_length=30,null=True) #Sch. type p-budg. form. ctre profit
    segment = models.CharField(max_length=30,null=True) #Segment
    name = models.CharField(max_length=30,null=True) #Désignation
    long_text = models.CharField(max_length=100,null=True) #Texte descriptif  
    profit_center_short_text_for_matchcode = models.CharField(max_length=100,null=True) #Désing. centre de pro
   

class SE16N_T001L(models.Model): #Model For File SE16N_T001L
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    division = models.IntegerField(null=True) #Division
    store = models.IntegerField(null=True) #Magasin
    descr_of_storage_loc = models.CharField(max_length=100,null=True) #Désignation magasin	
    store_level_deletion_indicator =models.CharField(max_length=20,null=True) #Secteur d'activité	
    negative_inventory=models.CharField(max_length=20,null=True) #Stks négatifs magas.	
    fix_stk_theo= models.CharField(max_length=20,null=True) #Fixer stk théo. mag.	    
    mrp_code = models.FloatField(null=True) #Code MRP		
    authorization_check = models.CharField(max_length=20,null=True) #Contrôle autorisat.	
    stor_resource = models.CharField(max_length=20,null=True) #Ressource magasin		
    management_missing_units = models.CharField(max_length=20,null=True)  #Gest. unités manut.	
    partner_store = models.CharField(max_length=20,null=True)  #Magasin partenaire		
    sales_organization = models.CharField(max_length=20,null=True)  #Organis. commerciale	
    distribution_channel = models.CharField(max_length=20,null=True)  #cannal de distrution		
    shipping_point_receiving_pt = models.CharField(max_length=20,null=True)  # Point expédition/réception		    
    vendor = models.CharField(max_length=20,null=True)  #fornisseur	
    customer = models.CharField(max_length=20,null=True)  #client	  
    business_system_of_mes = models.CharField(max_length=20,null=True) #Système de gestion du MES	
    inventory_management_type = models.CharField(max_length=20,null=True) # Tpe de gestion des stocks	
    license_number = models.CharField(max_length=20,null=True) #Numéro licence
    in_transit_assignment = models.CharField(max_length=20,null=True) # Affectation transit		
    tank_assgn = models.CharField(max_length=20,null=True) #Affectat. bac


class SE16N_T024(models.Model): #Model For File SE16N_T024
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by = models.IntegerField()
    uploaded_at= models.DateTimeField()
    purchasing_group = models.CharField(max_length=20,null=True) #Groupe d'acheteurs	
    description_p_group = models.CharField(max_length=20,null=True) #Désignat.grpe achet.	
    tel_no_purch_group = models.CharField(max_length=20,null=True) #N° tél.grpe achet.		
    output_device = models.CharField(max_length=20,null=True) #Unité de sortie	
    fax_number = models.CharField(max_length=20,null=True) #Numéro de télécopie	
    telephone = models.CharField(max_length=20,null=True) #Téléphone		
    extension = models.CharField(max_length=20,null=True) #Numéro de poste		
    e_mail_address = models.CharField(max_length=50,null=True) #Adresse e-mail	
    user_name = models.CharField(max_length=20,null=True) #Utilisateur	

class ZMM_CARNET_CDE_IS(models.Model): #Model For File  ZMM_CARNET_CDE_IS
     year=models.IntegerField(null=True)
     week=models.IntegerField(null=True)
     uploaded_by = models.IntegerField(null=True)
     uploaded_at= models.DateTimeField()
     request_no = models.CharField(max_length=30,null=True) #N° Demande		
     division = models.IntegerField(null=True) #Division
     store = models.IntegerField(null=True) #Magasin
     purchase_document = models.CharField(null=True,max_length=30)              #Document d'achat	  
     poste1 = models.CharField(null=True,max_length=30)              #Poste			
     due_date = models.CharField(null=True,max_length=20)              #Echéance		     
     vendor = models.CharField(max_length=50,null=True) #Fournisseur		
     vendor_name = models.CharField(max_length=50,null=True) #Nom Fournisseur		
     material = models.CharField(max_length=50,null=True) #Article			      
     designation_add_material = models.CharField(max_length=50,null=True) #Désignation add. art.			
     name = models.CharField(max_length=50,null=True) #Désignation			       
     transmission_info = models.DateTimeField(null=True)               #Info Transmission			
     validated_by = models.CharField(max_length=50,null=True) #Validé par			      
     priority = models.CharField(max_length=50,null=True) #Priorité de l'ordre			
     quantity = models.FloatField(null=True)              #Quantité de commande			       
     quantity_to_receive = models.FloatField(null=True)              #Quantité à réceptionner			
     date_of_purchase = models.DateTimeField(null=True)               #Date d'achat			       
     desired_date = models.DateTimeField(null=True)               #date souhaitée	
     original_delivery_date = models.DateTimeField(null=True)               #Date de livraison initiale				
     contractual_delivery_date = models.DateTimeField(null=True)               #Date de livraison contractulle	
     validated_delivery_date = models.DateTimeField(null=True)               #Date de livraison validée	
     confirmed_quantity = models.FloatField(null=True)              #Quantité confirmée
     comment = models.CharField(max_length=500,null=True) #Commentaire Appros				           
     expected_stock_week_w = models.FloatField(null=True)              #Stock Prévu Semaine S		
     expected_stock_week_w_1 = models.FloatField(null=True)              #Stock Prévu Semaine S+1		
     expected_stock_week_w_2 = models.FloatField(null=True)              #Stock Prévu Semaine S+2		
     expected_stock_week_w_3 = models.FloatField(null=True)              #Stock Prévu Semaine S+3		
     expected_stock_week_w_4 = models.FloatField(null=True)              #Stock Prévu Semaine S+4		
     expected_stock_week_w_5 = models.FloatField(null=True)              #Stock Prévu Semaine S+5		
     expected_stock_week_w_6 = models.FloatField(null=True)              #Stock Prévu Semaine S+6	
     expected_stock_week_w_7 = models.FloatField(null=True)              #Stock Prévu Semaine S+7	
     expected_stock_week_w_8 = models.FloatField(null=True)              #Stock Prévu Semaine S+8		
     expected_stock_week_w_9 = models.FloatField(null=True)              #Stock Prévu Semaine S+9		
     expected_stock_week_w_10 = models.FloatField(null=True)              #Stock Prévu Semaine S+10	
     expected_stock_week_w_11 = models.FloatField(null=True)              #Stock Prévu Semaine S+11	
     expected_stock_week_w_12 = models.FloatField(null=True)              #Stock Prévu Semaine S+12
     confirmation = models.CharField(max_length=30,null=True) #Confirmation ordre					
     estimated_delivery_time = models.CharField(null=True,max_length=20)              #Délai prévisionnel de livraison (en jrs)
     comment_vendor = models.CharField(max_length=500,null=True) #Commentaires fournisseur	
     element_otp = models.CharField(max_length=30,null=True) #Elément d'OTP		
     business_document = models.CharField(max_length=10,null=True) #Document commercial							
     poste2 = models.CharField(null=True,max_length=20)              #Poste			
     need_number= models.CharField(max_length=30,null=True)             # N° de besoin	
     net_price = models.FloatField(null=True)              #Prix net de la cde
     currency = models.CharField(max_length=10,null=True) #Devise
     price_basis = models.CharField(null=True,max_length=20)              #Base de prix	
     price_unit = models.CharField(max_length=10,null=True) #Unité de prix	
     net_order_value = models.FloatField(null=True)              #Valeur nette de cde	
     purchasing_document_type = models.CharField(max_length=10,null=True) # Type document achat	
     exception_message_number = models.CharField(null=True,max_length=20)              #Exception message numér
     exception_message = models.CharField(max_length=50,null=True) #Exception message	
     purchasing_group = models.CharField(max_length=50,null=True) #Groupe d'acheteurs	


class ZPP_MD_Stock(models.Model): #Model For File ZPP_MD_Stock
    year=models.IntegerField(null=True)
    year_week=models.CharField(max_length=30,null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    division = models.IntegerField(null=True) #Division
    material = models.CharField(max_length=30,null=True) #article	
    plan_date=models.DateTimeField(null=True)#Dates 
    # mrp_element = models.CharField(max_length=30,null=True)#Elément MRP
    # data_for_planning_element= models.CharField(max_length=30,null=True)#Données pr élément planif
    # action_message= models.CharField(max_length=30,null=True)#Message d'action
    Input_need=models.CharField(max_length=30,null=True)#Entrée / besoin
    # available_quantity= models.CharField(max_length=30,null=True)#Quantité disponible
    # reorder_date=models.DateTimeField(null=True)#Date réordonnanc.
    # vendor=models.CharField(max_length=30,null=True)#Fournisseur
    # customer=models.CharField(max_length=30,null=True)#Client
    # num_parcel=models.CharField(max_length=30,null=True) #col from ST 
    # delivery_qty=models.FloatField(null=True)#Col from ST
    # need_past=models.FloatField(null=True)
    # take_into_account_fr=models.CharField(max_length=15,null=True)
    # take_into_account_en=models.CharField(max_length=15,null=True)


class Stock_transit(models.Model): #Model For File Stock_transit
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    pExp= models.CharField(max_length=30,null=True) #PExp
    division = models.IntegerField(null=True) 	#Division Prenante
    transfer_code= models.CharField(max_length=30,null=True)#Cde Transfert
    poscde= models.CharField(max_length=30,null=True)#PosCde
    tLvr= models.CharField(max_length=30,null=True)#TLvr.
    actual_sm= models.CharField(max_length=30,null=True)#SM réelle
    delivery= models.CharField(max_length=30,null=True)#Livraison
    item= models.IntegerField(null=True)#Poste
    num_picking_UUID= models.IntegerField(null=True)	#N°Picking-UUID
    num_parcel= models.CharField(max_length=30,null=True)#N° Colis
    material = models.CharField(max_length=30,null=True)#Article
    delivery_qty=models.FloatField(null=True)	#Qté livraison
    uq=models.CharField(max_length=30,null=True)#UQ
    qty_delivered= models.IntegerField(null=True)#Qté livrée
    qty_received= models.IntegerField(null=True)#Qté Réceptionnée
    not_received= models.CharField(max_length=30,null=True)#Non Receptionné
    customer_order= models.CharField(max_length=30,null=True)#Cde Client (OF ou cde transf.)
    of_art_description= models.CharField(max_length=30,null=True)#Descrip.Art.OF
    msn= models.IntegerField(null=True)#MSN
    appro_Special= models.CharField(max_length=30,null=True)#Appro Spécial
    comment= models.CharField(max_length=30,null=True)#Commentaire
    n_of= models.CharField(max_length=30,null=True)#N° OF
    article_of= models.CharField(max_length=30,null=True)#Article OF

class ART_MARA_MARC(models.Model): #Model For File ART_MARA_MARC
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    scope_allocation=models.CharField(max_length=30,null=True) #col calculate at upload from cepc
    material = models.CharField(max_length=30,null=True) #article	
    material_designation= models.CharField(max_length=200,null=True) #Désignation article
    text_material= models.CharField(max_length=200,null=True) #Texte Article
    market_group= models.CharField(max_length=30,null=True) #Grpe march.
    division = models.IntegerField(null=True)  #Div
    ctrpr= models.CharField(max_length=30,null=True) #CtrPr
    typ_app	= models.CharField(max_length=30,null=True) #Typ.App.
    a_s	= models.CharField(max_length=30,null=True)#A.S
    tcy	= models.IntegerField(null=True)#TCy
    dfi	= models.IntegerField(null=True)#DFI
    dpr	= models.IntegerField(null=True)#DPr
    horiz= models.CharField(max_length=30,null=True)#Horiz
    mp= models.FloatField(null=True)#MP
    r= models.FloatField(null=True) #R
    tyar= models.CharField(max_length=30,null=True)	#TyAr
    nai= models.FloatField(null=True)#NAl
    i_c	= models.FloatField(null=True)#I/C
    aappr_def= models.FloatField(null=True)#AAppr/déf
    mgApp= models.FloatField(null=True)#MgApp
    mag= models.FloatField(null=True)#Mag.
    tl= models.CharField(max_length=30,null=True)	#TL
    fixed_batch	= models.FloatField(null=True) #Lot fixe
    uq1= models.CharField(max_length=30,null=True)#UQ
    security_stock= models.FloatField(null=True)#Stock sécurité
    uq2= models.CharField(max_length=30,null=True)#UQ
    tre= models.FloatField(null=True)#TRé
    gest= models.CharField(max_length=30,null=True)#Gest.
    di= models.CharField(max_length=30,null=True)#Di
    scrap= models.FloatField(null=True)#Rebut
    gac= models.CharField(max_length=30,null=True)#GAc
    profile= models.CharField(max_length=30,null=True) #Profil	
    prpiat= models.CharField(max_length=30,null=True)	#PrPiAt
    created_by= models.CharField(max_length=30,null=True)	#Créé par
    language= models.CharField(max_length=30,null=True)#Langue
    created_on=models.DateTimeField(null=True)#Créé le
    gcha= models.CharField(max_length=30,null=True)#GCha
    gs= models.CharField(max_length=30,null=True)#GS
    comparison_mode_of_the_requirements= models.CharField(max_length=30,null=True)#Mode de comparaison des besoin
    int_adjustment_upstream= models.FloatField(null=True) #Int.ajust.amont
    int_adjustment_downstream= models.FloatField(null=True) #Int.ajust.aval
    size_l_min= models.FloatField(null=True)#Taille l.min
    uq3= models.CharField(max_length=30,null=True)#UQ
    rounded_value= models.FloatField(null=True)#Val.arrondie
    uq4= models.CharField(max_length=30,null=True)	#UQ
    lot_size_mx= models.FloatField(null=True)#Taille lot mx
    uq5= models.CharField(max_length=30,null=True) #UQ
    maximum_stock= models.FloatField(null=True)#Stock maximum
    uq6= models.CharField(max_length=30,null=True)#UQ
    edge= models.CharField(max_length=30,null=True)#Chant
    typ= models.CharField(max_length=30,null=True)#TyP
    time_limit1= models.FloatField(null=True)	#Délai séc.
    time_limit2= models.FloatField(null=True) #Délai séc.
    recipient_ctrl= models.CharField(max_length=30,null=True) #Ctrl destinataire
    material_filled	= models.CharField(max_length=30,null=True) #Article rempl.
    dv= models.CharField(max_length=30,null=True) #Dv
    gml= models.CharField(max_length=30,null=True) #GML
    grpi= models.CharField(max_length=30,null=True) #GrPI
    abc	= models.CharField(max_length=30,null=True)#ABC
    uq7= models.CharField(max_length=30,null=True)#UQ
    wbs_element= models.CharField(max_length=30,null=True)	#Elément d'OTP
    grpa= models.CharField(max_length=30,null=True) #GrpA
    control_code= models.CharField(max_length=30,null=True) #Code pilotage
    product_hierarchy= models.CharField(max_length=30,null=True) #Hiérarch.produits
    gross_weight= models.FloatField(null=True) #Poids brut
    unp1= models.CharField(max_length=30,null=True) #UnP
    net_weight= models.FloatField(null=True)#Poids net
    unp2= models.CharField(max_length=30,null=True)#UnP
    no_ccr= models.CharField(max_length=30,null=True)#pas de CCR
    ccr_lot_size= models.FloatField(null=True)#Taille de lot du CCR
    uq8= models.CharField(max_length=30,null=True)#UQ
    district = models.CharField(max_length=30,null=True)  #col from CEPC
    profit_center_designation =models.CharField(max_length=100,null=True)#col from CEPC
    purchasing_group_designation=models.CharField(max_length=20,null=True)# Col from T024


class MDMA(models.Model):#Model For FIle MDMA
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)   
    material= models.CharField(max_length=30,null=True) #article	
    planning_unit= models.CharField(max_length=30,null=True)#Unité de planif.
    division = models.IntegerField(null=True)#U. planif. division
    planning_profile= models.CharField(max_length=30,null=True)#Profil planification
    planning_type= models.CharField(max_length=30,null=True)#Type planification
    manager= models.CharField(max_length=30,null=True)#Gestionnaire
    planning_group= models.CharField(max_length=30,null=True)#Groupe de planif.
    order_point= models.FloatField(null=True)#Point de commande
    planning_rate= models.CharField(max_length=30,null=True)#	Cadence de planif.
    fixed_planning_horizon= models.FloatField(null=True)#Horizon de planification fixe
    lot_size_calculation_key= models.CharField(max_length=30,null=True)#Clé calc. taille lot
    rounding_profile= models.CharField(max_length=30,null=True)#Profil d'arrondi
    rounding_value= models.FloatField(null=True)#Valeur arrondie
    minimum_lot_size= models.FloatField(null=True)#Taille lot minimale
    maximum_lot_size= models.FloatField(null=True)#Taille lot maximale
    maximum_stock= models.FloatField(null=True)#Stock maximum
    cycle= models.FloatField(null=True)#Cycle
    rejects_ss_ens= models.FloatField(null=True)#Rebut ss-ens. (%)
    special_supply= models.CharField(max_length=30,null=True)#Approvisionn.spécial
    production_store= models.CharField(max_length=30,null=True)	#Magasin production
    store_for_external_supply= models.CharField(max_length=30,null=True)#Mag.pour appro. ext.
    planning_calendar= models.CharField(max_length=30,null=True)#Calendrier planif.
    safety_stock= models.FloatField(null=True)#Stock de sécurité
    coverage_profile= models.CharField(max_length=30,null=True)#Profil de couverture
    safety_stock_actual_stock= models.FloatField(null=True)#Dél.séc./couv.réelle
    fixed_lot_size= models.FloatField(null=True)	#Taille de lot fixe
    fixed_lot_costs	= models.FloatField(null=True)#Coûts des lots fixes
    storage_cost_code= models.CharField(max_length=30,null=True)#Code coûts stockage
    service_rate = models.FloatField(null=True)#Taux de service (%)
    forecast_profile= models.CharField(max_length=30,null=True)#Profil de prévision
    ref_cons_val= models.CharField(max_length=30,null=True)#Val.consom.art.réf.
    un_plan_cons= models.CharField(max_length=30,null=True)#Un.planif. consomm.
    au= models.CharField(max_length=30,null=True)#Au
    multiplier= models.FloatField(null=True)#Multiplicateur
    suppr_indicator= models.CharField(max_length=30,null=True)#Témoin de suppr.
    prof_per_sec= models.CharField(max_length=30,null=True)#Prof. pér. dél. séc.
    dependent_needs_planner= models.CharField(max_length=30,null=True)#Planif. bes. dépend.
    reset_auto= models.CharField(max_length=30,null=True)#Réinitialiser autom.
    management_status= models.CharField(max_length=30,null=True)	#Statut de gestion
    correction_pow= models.CharField(max_length=30,null=True)#Coeff. correction
    safety_time= models.CharField(max_length=30,null=True)#Délai de sécurité
    for_apo= models.CharField(max_length=30,null=True)#Pour APO
    forecast_delivery_time= models.CharField(max_length=30,null=True)#Délai prév. livrais.
    take_into_account_the_expected_delivery_time= models.CharField(max_length=30,null=True)#Tenir cpte du délai prév.livr.


class SoftDeleteManager(models.Manager): #Manager to softdelete Model
    # def deleted_object(self):
    #     return super().get_queryset().filter(deleted=True)
    # def nodeleted_object(self):
    #     return super().get_queryset().filter(deleted=False)
       def get_queryset(self):
           return super().get_queryset().filter(deleted=False)

class Soft_delete(models.Model): #model info 
    # uploaded_by= models.IntegerField(null=True, default='1')
    # uploaded_at= models.DateTimeField(null=True, auto_now_add=True)
    deleted=models.BooleanField(default=False)
    deleted_by=models.IntegerField(null=True)
    deleted_on=models.DateTimeField(null=True)
    objects=models.Manager()
    undeleted_objects=SoftDeleteManager()
    def soft_delete(self):
        self.deleted = True
        self.save()
    def soft_delete(self):
        self.deleted_on = datetime.now()
        self.save()
    def soft_delete(self):
        self.deleted_by = 1
        self.save()
    class Meta:
        abstract=True


class Core(Soft_delete): #Model For Core
    created_on=models.DateTimeField()
    created_by=models.IntegerField(default=1)
    updated_by=models.IntegerField(default=1)
    updated_on=models.DateTimeField()
    material = models.CharField(max_length=10,null=True) #Référence article	
    division=models.CharField(max_length=30,null=True)
    program=models.CharField(max_length=30,null=True)
    supplier=models.CharField(max_length=30,null=True)
    part_number=models.FloatField(null=True)
    type_of_alert=models.CharField(max_length=30,null=True)
    requested_date=models.DateTimeField()
    needed_quantity=models.FloatField(null=True)
    subject=models.TextField(null=True)
    status=models.CharField(max_length=30,null=True,default='To do') #Default To do
    closing_date=models.DateTimeField(null=True)
    duration_of_the_event=models.CharField(max_length=30,null=True)

class CoreHistory(models.Model): #Model For Core history
    core=models.ForeignKey(Core,on_delete=models.CASCADE)
    created_on=models.DateTimeField()
    created_by=models.IntegerField(default=1)
    comment=models.TextField(null=True)
    action=models.CharField(max_length=30,null=True)

class Mrp_element(Soft_delete): #Model For mrp_element
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    mrp_element = models.CharField(max_length=30,null=True) #élément mrp
    fr = models.CharField(max_length=30,null=True) #FR
    en = models.CharField(max_length=30,null=True) #EN
    take_into_account =models.CharField(max_length=15,null=True) #Take into account

class Apro_spec(Soft_delete):#Model For  apro spec
    year=models.IntegerField(null=True)
    week=models.IntegerField(null=True)
    uploaded_by=models.IntegerField(null=True)
    uploaded_at=models.DateTimeField(null=True)
    appro_type=models.CharField(max_length=30,null=True) #Type appro
    division = models.IntegerField(null=True) #Division