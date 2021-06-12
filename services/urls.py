"""Service_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from .views import Service_detail, Service_add, Service_update

app_name = 'service'

urlpatterns = [
    #SERVICES CRUD + list
    path('dodaj', Service_add.as_view(), name='add'),
    path('<int:pk>/edytuj', Service_update.as_view(), name='update'),
    path('<int:pk>', Service_detail.as_view(), name='detail'),
]
