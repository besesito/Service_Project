from django.views import generic
from .models import Customer
from .forms import CustomerForm
from django.contrib.messages.views import SuccessMessageMixin
from services.models import Service
import json

# Create your views here.

class Customer_add(SuccessMessageMixin, generic.edit.CreateView):
    model = Customer
    template_name = 'customers/add.html'
    form_class = CustomerForm
    success_message = "Klient został pomyślnie dodany"


class Customer_update(SuccessMessageMixin, generic.UpdateView):
    model = Customer
    template_name = 'customers/update.html'
    form_class = CustomerForm
    success_message = 'Klient został pomyślnie zedytowany'


class Customer_detail(generic.DetailView):
    model = Customer
    template_name = 'customers/detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(customer=self.object).order_by('date')
        return context

class Customer_list(generic.ListView):
    model = Customer
    template_name = 'customers/list.html'
    context_object_name = 'customers'
    paginate_by = 50
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Customer.objects.values()), default=str)
        return context






