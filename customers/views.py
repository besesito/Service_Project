from django.shortcuts import render
from django.views import generic
from .models import Customer
from .forms import CustomerForm


# Create your views here.

class Add_customer(generic.edit.CreateView):
    model=Customer
    template_name='customers/add.html'
    fields='__all__'
    form = CustomerForm