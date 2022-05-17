from django.urls import path
from administration import views
urlpatterns = [
    path('files_list',views.files_list,name='files_list'),
    path('file_details/<str:namefile>/',views.file_details,name='file_details'),
    path('delete_file/<int:year>/<int:week>/<str:namefile>',views.delete_file,name='delete_file'),
    path('file_content/<int:year>/<int:week>/<str:namefile>',views.file_content,name='file_content'),
    #URLs Mrp _element
    path('mrp_element',views.mrp_element,name='mrp_element'), 
    path ('mrp_element/create',views.create_mrp_element,name='create_mrp_element'),
    path('mrp_element/<int:pk>/update',views.update_mrp_element,name='update_mrp_element'),
    path('mrp_element/<int:pk>/delete',views.delete_mrp_element,name='delete_mrp_element'),
    #CRUD Apro spec 
    path('apro_spec',views.apro_spec,name='apro_spec'), 
    path ('apro_spec/create',views.create_apro_spec,name='create_apro_spec'),
    path('apro_spec/<int:pk>/update',views.update_apro_spec,name='update_apro_spec'),
    path('apro_spec/<int:pk>/delete',views.delete_apro_spec,name='delete_apro_spec'),
]
