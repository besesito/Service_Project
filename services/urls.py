from django.contrib import admin
from django.urls import include, path
from .views import Service_detail, Service_add, Service_update, Service_list, Service_delete, My_services

app_name = 'service'

urlpatterns = [
    #SERVICES CRUD + list
    path('dodaj', Service_add.as_view(), name='add'),
    path('<int:pk>/edytuj', Service_update.as_view(), name='update'),
    path('<int:pk>/usun', Service_delete.as_view(), name='delete'),
    path('<int:pk>', Service_detail.as_view(), name='detail'),
    path('', Service_list.as_view(), name='list'),
    path('moje', My_services.as_view(), name='my_services'),
]
