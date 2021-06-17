from django.db import models
from django.contrib.auth.models import User
from customers.models import Customer
from django.shortcuts import reverse
from Service_Project.validators import intiger_validate
# Create your models here.

class Kind_of_service(models.Model):
    class Meta:
        ordering=['kind']
    kind = models.CharField(max_length=100)
    def __str__(self):
        return self.kind


class Status(models.Model):
    class Meta:
        ordering=['status']
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.status


class Service(models.Model):
    class Meta:
        ordering=['status', 'date']
    kind = models.ForeignKey(Kind_of_service, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    adress = models.CharField(max_length=300, blank=True)
    phone_number = models.CharField(blank=True, max_length=12, validators=[intiger_validate])
    description = models.TextField(blank=True)
    responsible_persons = models.ManyToManyField(User, related_name='responsible_persons_user')
    notifications = models.ManyToManyField(User, blank=True, related_name='notifications_user')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    def __str__(self):
        return self.customer.name
    def get_absolute_url(self):
        return reverse('service:detail', kwargs={'pk': self.pk})
