from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Tag(models.Model):
    class Meta:
        ordering=['tag']
    tag = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return (self.tag)
    def get_absolute_url(self):
        return reverse('customer:add')

class Platform(models.Model):
    class Meta:
        ordering=['platform']
    platform = models.CharField(max_length=50)
    def __str__(self):
        return (self.platform)

class Customer(models.Model):
    class Meta:
        ordering=['name']

    name = models.CharField(unique=True, max_length=200)
    alias = models.CharField(blank=True, null=True, unique=True, max_length=100)
    nip = models.CharField(blank=True, null=True, unique=True, max_length=20)
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(blank=True, null=True, unique=True, max_length=12)
    address = models.CharField(blank=True, max_length=200)
    contract = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    platforms = models.ManyToManyField(Platform, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.name)

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = None
        if not self.nip:
            self.nip = None
        if not self.email:
            self.email = None
        if not self.phone_number:
            self.phone_number = None
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('customer:detail', kwargs={'pk': self.pk})