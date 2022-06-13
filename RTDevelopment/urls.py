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
    path('admin/', admin.site.urls),
    path('machines/',views.machine_list_view, name='machine'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    path('persos/',views.personnel_list_view, name='employe'),
    path('perso/<pk>',views.personnel_detail_view,name='employe-detail'),
    path('add-machine',views.machine_add_form,name='add-machine'),
    path('add-employe', views.personnel_add_form,name='add-employe')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
