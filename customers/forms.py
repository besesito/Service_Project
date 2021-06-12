from django.forms import ModelForm
from .models import Customer, Platform, Tag
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        help_texts = {
            'contract': ('Data końcowa umowy'),
            'tags': ('Tagi do łatwej identyfikacji klienta'),
            'alias': ('Skrócona nazwa klienta')
        }
        labels = {
            'address': ('Adres'),
            'name': ('Nazwa'),
            'nip': ('NIP'),
            'phone_number': ('Numer telefonu'),
            'tags': ('Tagi klienta'),
            'platforms': ('Platformy'),
            'contract': ('Okres umowy')
        }
        widgets = {
            'contract': forms.DateInput(attrs={'type': 'date'})
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
