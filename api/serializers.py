from rest_framework import serializers
from customers.models import Customer
from services.models import Service, Kind_of_service, Status
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind_of_service
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class ReadServiceSerializer(serializers.ModelSerializer):
    kind = KindSerializer()
    customer = CustomerSerializer()
    status = StatusSerializer()
    author = UserSerializer()
    class Meta:
        model = Service
        fields = '__all__'

class WriteServiceSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(slug_field='status', queryset=Status.objects.all())
    kind = serializers.SlugRelatedField(slug_field='kind', queryset=Kind_of_service.objects.all())
    class Meta:
        model = Service
        fields = '__all__'
