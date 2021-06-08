from django.forms import ModelForm
from .models import Customer, Platform, Tag
from django.core import validators

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        help_texts = {
            'name': ('Oficjalna nazwa klienta'),
            'alias': ('Skrótowa nazwa w celu łatwiejszej identyfikacji'),
            'contract': ('Data końcowa umowy')
        }
        labels = {
            'name': ('Nazwa'),
            'nip': ('NIP'),
            'phone_number': ('Numer telefonu'),
            'tags': ('Tagi klienta'),
            'platforms': ('Platformy'),
            'contract': ('Okres umowy')
        }

class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
        labels = {
            'tag': 'Dodaj tag'
        }

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'
        labels = {
            'platform': 'Platforma'
        }