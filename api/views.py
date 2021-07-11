from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

from .serializers import CustomerSerializer, WriteServiceSerializer, ReadServiceSerializer
from customers.models import Customer
from services.models import Service


class CustomerModelViewSet(ModelViewSet):
	queryset = Customer.objects.all()
	serializer_class = CustomerSerializer

class ServiceModelViewSet(ModelViewSet):
	queryset = Service.objects.select_related("customer", "kind", "status", "author")
	filter_backends = [filters.SearchFilter, filters.OrderingFilter]
	search_fields = ["customer__name"]
	ordering_fields = ['date']

	def get_serializer_class(self):
		if self.action in ('list', 'retrieve'):
			return ReadServiceSerializer
		return WriteServiceSerializer