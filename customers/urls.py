from django.urls import include, path
from .views import Customer_add, Customer_update, Customer_detail, Customer_list
app_name = 'customer'

urlpatterns = [
    #CUSTOMERS CRUD + list
    path('', Customer_list.as_view(), name='list'),
    path('dodaj', Customer_add.as_view(), name='add'),
    path('<int:pk>/edytuj', Customer_update.as_view(), name='update'),
    path('<int:pk>', Customer_detail.as_view(), name='detail'),
]
