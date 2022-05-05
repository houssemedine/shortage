from django.urls import path
from administration import views
urlpatterns = [
    path('files_list',views.files_list,name='files_list'),
    path('file_details/<str:namefile>/',views.file_details,name='file_details'),
    path('delete_file/<int:year>/<int:week>/<str:namefile>',views.delete_file,name='delete_file'),
    path('file_content/<int:year>/<int:week>/<str:namefile>',views.file_content,name='file_content')

]
