from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Service)
admin.site.register(Kind_of_service)
admin.site.register(Status)