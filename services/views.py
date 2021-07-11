from django.urls import reverse_lazy
from django.views import generic
from .models import Service
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .forms import ServiceForm
from customers.models import Customer
from django.core import serializers


class Service_add(SuccessMessageMixin, generic.CreateView):
    model = Service
    template_name = 'services/add.html'
    form_class = ServiceForm
    success_message = 'Usługa została pomyślnie dodana'

    def form_valid(self, form):
        if not form.cleaned_data.get('phone_number'):
            if Customer.objects.get(name=form.cleaned_data.get('customer')).phone_number:
                form.instance.phone_number = Customer.objects.get(name=form.cleaned_data.get('customer')).phone_number
        if not form.cleaned_data.get('adress'):
            if Customer.objects.get(name=form.cleaned_data.get('customer')).address:
                form.instance.adress = Customer.objects.get(name=form.cleaned_data.get('customer')).address
        form.instance.author = self.request.user
        return super().form_valid(form)


class Service_update(SuccessMessageMixin, generic.UpdateView):
    model = Service
    template_name = 'services/update.html'
    form_class = ServiceForm
    success_message = 'Usługa została pomyślnie zaktualizowana'


class Service_delete(generic.DeleteView):
    model = Service
    template_name = 'services/delete.html'
    success_url = reverse_lazy('service:list')
    context_object_name = 'service'
    success_message = 'Usługa został pomyślnie usunięta'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(Service_delete, self).delete(request, *args, **kwargs)


class Service_detail(generic.DetailView):
    model = Service
    template_name = 'services/detail.html'
    context_object_name = 'service'


class Service_list(generic.ListView):
    model = Service
    template_name = 'services/list.html'
    
    context_object_name = 'services'
    paginate_by = 50
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['qs_json'] = serializers.serialize("json", Service.objects.all(), use_natural_foreign_keys=True)
    #     return context


class My_services(generic.ListView):
    model = Service
    template_name = 'services/my_services.html'
    context_object_name = 'services'
    paginate_by = 50

    def get_queryset(self):
        return Service.objects.filter(responsible_persons=self.request.user)
