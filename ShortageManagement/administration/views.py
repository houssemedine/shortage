from django.shortcuts import render,redirect
from django.apps import apps
import pandas as pd
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def files_list(request):
    models_name=apps.all_models['shortage']#to get all models in shortage
    return render(request,r'administration\files_list.html' ,{'models_name':models_name})

def file_details(request,namefile):
    Model=apps.get_model('shortage',namefile) #to get model from shortage
    data=Model.objects.values('year','week','uploaded_by','uploaded_at').distinct()
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

