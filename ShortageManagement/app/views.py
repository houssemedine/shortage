# Create your views here.
from io import StringIO
from app.models import MB52
from django.shortcuts import render
import pandas as pd
import openpyxl 
import psycopg2
import time
from datetime import datetime


def home(request):
    start=time.time()
    import_file_MB52()
    end=time.time()
    total=end-start
    mb52_data=MB52.objects.all().count()
    print('*'*50)
    print(total)
    print(mb52_data)
    print('*'*50)

    return render(request,'app\index.html')

#def import_file():
    #Connection to DB
    #conn= psycopg2.connect(host='localhost', dbname='latecoere_db', user= 'postgres', password='sahar',port='5432')
    #Read file
    #file=r'C:\Users\bibas\Downloads\person.xlsx' 
    #df = pd.read_excel(file) # to read file excel #dataframe
    # df=df.to_csv(r'C:\Users\bibas\Downloads\testperson.csv',index=True) # To download a file as CSV

    #df=df.to_csv(index=False,header=None) #To convert to csv / index=False => without ID

    #student=StringIO()
    #student.write(df)
    #student.seek(0)
    #with conn.cursor() as curs:
        #curs.copy_from(
            #file=student,
            #table="app_person",
            #columns=[
                #'first_name',
                #'last_name',
                #'age',
                #'moyenne'
            #],
           # null='',
           # sep=','
        #)
    #conn.commit()

#function for import file MB52
def import_file_MB52():
    #connection to DB 
    conn= psycopg2.connect(host='localhost', dbname='shortagemanquant_db', user='postgres', password='sahar',port='5432')
    #Read file
    file=r'C:\Users\bibas\OneDrive\Bureau\PFE\inputSAP\MB52.xlsx'
    df = pd.read_excel(file) # to read file excel
    df=df.to_csv(index=False,header=None) #To convert to csv
    mb=StringIO()
    mb.write(df)
    mb.seek(0)
    with conn.cursor() as curs:
        curs.copy_from(
            file=mb,
            table="app_mb52",
            columns=[
            #    'uploaded_by ',
            #    'uploaded_at',
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
    conn.commit()


    


    

