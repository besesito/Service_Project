from django.db import models
from django.shortcuts import reverse
from Service_Project.validators import intiger_validate
from django.db.models.functions import Lower
from django.contrib.auth.models import User


class Tag(models.Model):
    class Meta:
        ordering = [Lower('tag')]

    tag = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return (self.tag)


class Platform(models.Model):
    class Meta:
        ordering = [Lower('platform')]

    platform = models.CharField(max_length=50)

    def __str__(self):
        return (self.platform)


class Customer(models.Model):
    class Meta:
        ordering = [Lower('name')]

    name = models.CharField(unique=True, max_length=200)
    alias = models.CharField(blank=True, null=True, unique=True, max_length=100)
    nip = models.CharField(blank=True, null=True, unique=True, max_length=20, validators=[intiger_validate])
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=12, validators=[intiger_validate])
    address = models.CharField(blank=True, max_length=200)
    contract = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    platforms = models.ManyToManyField(Platform, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse('customer:detail', kwargs={'pk': self.pk})

class Image(models.Model):
    image = models.ImageField(upload_to ='images')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ("{} by {}".format(self.customer, self.author))

    def get_absolute_url(self):
        return reverse('customer:detail', kwargs={'pk': self.customer.id})