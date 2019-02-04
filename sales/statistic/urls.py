from django.urls import path

from . import views

urlpatterns = [
    path('logout/', views.logout_my, name='logout'),
    path('get_client_info/', views.get_client_info, name='get_client_info'),
    path('main/', views.get_main, name='get_main'),
    path('', views.index, name='index'),
]