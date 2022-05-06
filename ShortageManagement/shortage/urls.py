from django.urls import path
from shortage import views
urlpatterns = [
    #Import Files
    path('upload',views.upload,name='upload'), #To upload fils

    #CRUD Core
    path('core',views.core,name='core'), 
    path ('core/create',views.create_core,name='create_core'),
    path('core/<int:pk>/update',views.update_core,name='update_core'),
    path('core/<int:pk>/delete',views.delete_core,name='delete_core'),
    path('core/<int:pk>/history/',views.core_history,name='core_history'),
    path('core/<int:pk>/save_history/',views.save_core_history,name='save_core_history'),

    #Result 
    path ('overview',views.overview,name='overview'), #table of result 
    # path('viewall/<int:pk>',views.viewall,name='viewall')
    path ('kpi',views.kpi,name='shortage_kpi'), #table of result 



]
