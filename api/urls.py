from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('customers-list/', views.customerList, name="customers-list"),
	path('customer-detail/<str:pk>/', views.customerDetail, name="customer-detail"),
	path('customer-create/', views.customerCreate, name="customer-create"),
    path('customer-update/<str:pk>/', views.customerUpdate, name="customer-update"),
	path('customer-delete/<str:pk>/', views.customerDelete, name="customer-delete"),
]