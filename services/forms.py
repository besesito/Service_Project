from .models import Service
from django import forms


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ['author']
        help_texts = {
            'notifications': ('Osoby które mają być informowane o zadaniu'),
            'phone_number': ('Jeżeli zostawisz pusty zostanie użyty z profilu klienta'),
            'adress': ('Jeżeli zostawisz pusty zostanie użyty z profilu klienta'),
        }
        labels = {
            'kind': ('Rodzaj usługi'),
            'phone_number': ('Numer telefonu'),
            'responsible_persons': ('Osoby odpowiedzialne'),
            'notifications': ('Powiadomienia'),
            'customer': ('Klient'),
            'date': ('Data'),
            'time': ('Godzina'),
            'adress': ('Adres'),
            'description': ('Opis zadania'),
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }
