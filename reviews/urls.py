from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machines/',views.machine_list_view, name='machines'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    path('persos/',views.personnel_list_view, name='perso'),
    path('perso/<pk>',views.personnel_detail_view,name='perso-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('add-personnel',views.personnel_add_form,name='add-personnel'),
    path('register',views.register,name='register'),
    path('login', views.login,name='login'),
]