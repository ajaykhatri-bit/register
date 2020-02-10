
from django.urls import path
from .import views

urlpatterns = [
    path('api/', views.api_data, name = "api_data"),
    path('update/<int:pk>/', views.update_api_data, name = 'update_api_data'),
    path('delete/<int:pk>/', views.delete_api_data, name = 'delete_api_data'),
    path('post/', views.post_api_data, name = 'post_api_data'),
    path('api/software/<int:PAGENO>/<int:SIZE>',views.api_software,name="api_software_data"),
    # path('api/posts/<int:PAGENO>/<int:SIZE>',views.api_post,name="api_posts_data"),

]
