from django.urls import path, include
from .import views

app_name = "download"
urlpatterns = [
 path('download/', views.download, name = "download"),
 path('download/upload/',views.upload_stw, name="upload_stw"),
 path('download/soft_list/', views.soft_list, name="soft_stw"),
 path('download/<int:pk>', views.delete_stw,name="delete_stw"),
#  path("api/", views.api_data, name="api_data"),
#  path('change/<int:pk>', views.update_api_data, name="update_api_data")
]