from .serializers import CustomerSerializer, ServiceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customers.models import Customer
from services.models import Service

#API
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'CustomerList':'/customers-list/',
		'CustomerDetail':'/customer-detail/<str:pk>/',
		'CustomerCreate':'/customer-create/',
		'CustomerUpdate':'/customer-update/<str:pk>/',
		'CustomerDelete':'/customer-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def customerList(request):
	customers = Customer.objects.all().order_by('-id')
	serializer = CustomerSerializer(customers, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def customerDetail(request, pk):
	customers = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(customers, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def customerCreate(request):
	serializer = CustomerSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def customerUpdate(request, pk):
	customer = Customer.objects.get(id=pk)
	serializer = CustomerSerializer(instance=customer, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def customerDelete(request, pk):
	customer = Customer.objects.get(id=pk)
	customer.delete()

	return Response('Item succsesfully delete!')
