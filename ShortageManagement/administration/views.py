from django.shortcuts import render,redirect
from django.apps import apps
import pandas as pd
from shortage.forms import  Form_mrp,Form_apro
from shortage.models import Mrp_element,Apro_spec
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from datetime import datetime


# Create your views here.
def files_list(request):
    models_name=apps.all_models['shortage']#to get all models in shortage
    return render(request,r'administration\files_list.html' ,{'models_name':models_name})

def file_details(request,namefile):
    Model=apps.get_model('shortage',namefile) #to get model from shortage
    data=Model.objects.values('year','week').distinct()
    return render(request,r'administration\file_details.html',{'data':data,'namefile':namefile})

def delete_file(request,week,year,namefile):#To delete file
    Model=apps.get_model('shortage',namefile) #to get models from shortage
    data=Model.objects.filter(week=week,year=year).order_by('year')
    data.delete()
    return redirect('file_details',namefile=namefile)

def file_content(request,week,year,namefile):
    Model=apps.get_model('shortage',namefile)
    data=Model.objects.filter(week=week,year=year).values_list()
    fields=[field.name for field in Model._meta.get_fields()] #get fields from model 
    page = request.GET.get('page',1)
    paginator=Paginator(data,30) # 30 is number of element in one page
    try:
        data=paginator.page(page)
    except PageNotAnInteger:
        data=paginator.page(1)
    except EmptyPage:
        data=paginator.page(paginator.num_pages)
    return render(request,r'administration\file_content.html',{'data':data,'week':week,'year':year,'namefile':namefile,'fields':fields})
#CRUD mrp element
def mrp_element(request):#show list of mrp element
    filter=""
    if  (request.method == 'POST') :
        data=Mrp_element.objects.all().order_by('-id')
        filter='all'
    else:
        data=Mrp_element.undeleted_objects.all()
    return render(request,r'administration\mrp_element.html',{'data':data,'filter':filter})

def create_mrp_element(request):#Create mrp element
    if  (request.method == 'POST') :
        mrp_element=request.POST['mrp_element']
        data=Mrp_element.undeleted_objects.all().filter(mrp_element=mrp_element)
        print(data.first())
        if data:
            messages.warning(request,'Mrp element is already exist !')
        else:
            form_mrp = Form_mrp(request.POST)
            if form_mrp.is_valid():
                instance=form_mrp.save(commit=False)
                instance.created_on =datetime.now()
                instance.updated_on =datetime.now()
                instance.created_by=1
                instance.save()
                messages.success(request,'Mrp element added sucessfully')
                return redirect('mrp_element')

    return render(request,'administration\create_mrp_element.html',{'form_mrp' : Form_mrp})

def delete_mrp_element(request,pk): #function soft-delete for mrp element
    mrp_element=Mrp_element.objects.get(id=pk)
    mrp_element.deleted=True
    mrp_element.deleted_on=datetime.now()
    mrp_element.deleted_by=1
    mrp_element.save()
    return redirect('mrp_element')

def update_mrp_element(request,pk): #function for update mrp element
    mrp=Mrp_element.objects.get(id=pk)
    form_mrp=Form_mrp(instance=mrp)
    if (request.method=='POST'):
        form_mrp = Form_mrp(request.POST,instance=mrp)
        mrp_element=request.POST['mrp_element']
        data=Mrp_element.undeleted_objects.all().filter(mrp_element=mrp_element)
        print(data.first())
        if data:
            messages.warning(request,'Mrp element is already exist !')
            # return render(request,'shortage/core_history.html',{'pk':data.first().id,'data':data})
            return redirect('mrp_element')
        else:
            if form_mrp.is_valid():
                form_mrp.save()
                messages.success(request,"Mrp element updated successfully!")
                return redirect('mrp_element')
            else:
                messages.error(request, 'Invalid form submission.') 
    return render(request,'administration/update_element_mrp.html',{'mrp' : mrp,'form_mrp' : form_mrp})


#CRUD APPRO SPEC
def apro_spec(request): #function  for read appro spec
        filter=""
        if  (request.method == 'POST') :
            data=Apro_spec.objects.all().order_by('-id')
            filter='all'
        else:
            data=Apro_spec.undeleted_objects.all()
        return render(request,r'administration\apro_spec.html',{'data':data,'filter':filter})

def create_apro_spec(request): #function for creaate appro spec
     if  (request.method == 'POST') :
        appro_type=request.POST['appro_type']
        data=Apro_spec.undeleted_objects.all().filter(appro_type=appro_type)
        print(data.first())
        if data:
            messages.warning(request,'Appro spec is already exist !')
        else:
            form_apro = Form_apro(request.POST)
            print(form_apro)
            if form_apro.is_valid():
                instance=form_apro.save(commit=False)
                instance.created_on =datetime.now()
                instance.updated_on =datetime.now()
                instance.created_by=1
                instance.save()
                messages.success(request,'Appro spec added sucessfully')
                return redirect('apro_spec')
            else:
                messages.warning(request,'Data not valid!')
                return redirect('apro_spec')

     return render(request,'administration\create_apro_spec.html',{'form_apro' : Form_apro})


def update_apro_spec(request,pk): #function for update appro spec
    appro=Apro_spec.objects.get(id=pk)
    form_apro=Form_apro(instance=appro)
    if (request.method=='POST'):
        form_apro = Form_apro(request.POST,instance=appro)
        appro_type=request.POST['appro_type']
        data=Apro_spec.undeleted_objects.all().filter(appro_type=appro_type)
        print(data.first())
        if data:
            messages.warning(request,'appro spec is already exist !')
            # return render(request,'shortage/core_history.html',{'pk':data.first().id,'data':data})
            return redirect('apro_spec')
        else:
            if form_apro.is_valid():
                form_apro.save()
                messages.success(request,"appro spec updated successfully!")
                return redirect('apro_spec')
            else:
                messages.error(request, 'Invalid form submission.') 
    return render(request,'administration/update_apro_spec.html',{'appro' : appro,'form_apro' : form_apro})


def delete_apro_spec(request,pk): #function soft-delete for appro spec 
    apro_spec=Apro_spec.objects.get(id=pk)
    apro_spec.deleted=True
    apro_spec.deleted_on=datetime.now()
    apro_spec.deleted_by=1
    apro_spec.save()
    return redirect('apro_spec')
    

