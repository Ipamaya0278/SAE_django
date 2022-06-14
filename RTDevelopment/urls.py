"""RTDevelopment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reviews import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('machines/',views.machine_list_view, name='machines'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    path('persos/',views.personnel_list_view, name='perso'),
    path('perso/<pk>',views.personnel_detail_view,name='perso-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('add-personnel',views.personnel_add_form,name='add-personnel'),
    path('register',views.register,name='register'),
    path('login', views.login,name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
