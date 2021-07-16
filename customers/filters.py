import django_filters
from .models import Customer, Platform, Tag
from django import forms

class CustomerFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label="Nazwa", lookup_expr='icontains')
    alias = django_filters.CharFilter(label="Alias", lookup_expr='icontains')
    nip = django_filters.CharFilter(label="NIP", lookup_expr='icontains')
    platforms = django_filters.ModelMultipleChoiceFilter(label="Platformy", queryset=Platform.objects.all(), widget=forms.CheckboxSelectMultiple, conjoined=True)
    tags = django_filters.ModelMultipleChoiceFilter(label="Tagi", queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, conjoined=True)

    class Meta:
        model = Customer
        fields = [
            'name',
            'alias',
            'nip',
            'platforms',
            'tags'
            ]
        

    
