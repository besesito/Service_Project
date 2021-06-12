from django.shortcuts import render
from django.views import generic
from .models import Customer, Tag
from .forms import CustomerForm, TagForm, PlatformForm
from django.contrib.messages.views import SuccessMessageMixin
from services.models import Service

# Create your views here.

class Customer_add(SuccessMessageMixin, generic.edit.CreateView):
    model=Customer
    template_name='customers/add.html'
    form_class = CustomerForm
    success_message = "Klient został pomyślnie dodany"

    def get_context_data(self, **kwargs):
        context = super(Customer_add, self).get_context_data(**kwargs)
        context.update({'TagForm': TagForm, 'PlatformForm': PlatformForm})
        return context


class Customer_update(SuccessMessageMixin, generic.UpdateView):
    model = Customer
    template_name = 'customers/update.html'
    form_class = CustomerForm
    success_message = 'Klient został pomyślnie zedytowany'

    def get_context_data(self, **kwargs):
        context = super(Customer_update, self).get_context_data(**kwargs)
        context.update({'TagForm': TagForm, 'PlatformForm': PlatformForm})
        return context


class Customer_detail(generic.DetailView):
    model=Customer
    template_name='customers/detail.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super(Customer_detail, self).get_context_data(**kwargs)
        services = Service.objects.filter(customer=self.object).order_by('date_time')
        print(services)
        context.update({'services': services})
        return context

class Customer_list(generic.ListView):
    model=Customer
    template_name='customers/list.html'
    context_object_name = 'customers'
    paginate_by=50


class Tag_add(SuccessMessageMixin, generic.edit.CreateView):
    model=Tag
    template_name='customers/add_tag.html'
    form_class = TagForm
    success_message = "Tag został pomyślnie dodany"


class Tag_detail(generic.DetailView):
    model=Tag
    template_name='customers/tag_detail.html'
    context_object_name = 'tag'

