from django.shortcuts import render
from django.views import generic
from .models import Kind_of_service, Service
from django.contrib.messages.views import SuccessMessageMixin
from .forms import ServiceForm
from customers.models import Customer

# Create your views here.

class Service_add(SuccessMessageMixin, generic.CreateView):
    model = Service
    template_name = 'services/add.html'
    form_class = ServiceForm
    success_message = 'Usługa została pomyślnie dodana'
    def form_valid(self, form):
        if not form.cleaned_data.get('phone_number'):
            if Customer.objects.get(name=form.cleaned_data.get('customer')).phone_number:
                form.instance.phone_number = Customer.objects.get(name=form.cleaned_data.get('customer')).phone_number
        return super().form_valid(form)



class Service_update(SuccessMessageMixin, generic.UpdateView):
    model = Service
    template_name = 'services/update.html'
    form_class = ServiceForm
    success_message = 'Usługa została pomyślnie zaktualizowana'


class Service_detail(generic.DetailView):
    model=Service
    template_name='services/detail.html'
    context_object_name = 'service'
