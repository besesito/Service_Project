from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register('customer', views.CustomerModelViewSet, basename='customer')
router.register('service', views.ServiceModelViewSet, basename='service')

urlpatterns = [
] + router.urls