from django.shortcuts import render
from django.views import generic
from .models import Customer, Tag
from .forms import CustomerForm, TagForm, PlatformForm


# Create your views here.

class Customer_add(generic.edit.CreateView):
    model=Customer
    template_name='customers/add.html'
    form_class = CustomerForm

    def get_context_data(self, **kwargs):
        context = super(Customer_add, self).get_context_data(**kwargs)
        context.update({'TagForm': TagForm,
                        'PlatformForm': PlatformForm
                        })
        return context

class Customer_detail(generic.DetailView):
    model=Customer
    template_name='customers/detail.html'
    context_object_name = 'customer'

class Customer_list(generic.ListView):
    model=Customer
    template_name='customers/list.html'
    context_object_name = 'customers'
    paginate_by=50

class Tag_add(generic.edit.CreateView):
    model=Tag
    template_name='customers/add_tag.html'
    form_class = TagForm

class Tag_detail(generic.DetailView):
    model=Tag
    template_name='customers/tag_detail.html'
    context_object_name = 'tag'

