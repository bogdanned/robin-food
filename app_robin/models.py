from __future__ import unicode_literals

from django.db import models

# Create your models here.

class newCustomer(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    name = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Name')
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone_number = models.CharField(max_length = 12, null=True, blank = True, verbose_name = 'Phone Number')
    address = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Adress')
    position = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'ID Number(NIF/NIE)')
    image = models.ImageField(upload_to="images/", null=True, blank = True)
    description = models.CharField(max_length = 5000, null=True, blank = True, verbose_name = 'Description')


class newProduct(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    name = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Nombre')
    quantity = models.IntegerField(blank = False, null = False, verbose_name = 'Cantidad')
    price = models.IntegerField(blank=True, null=True)
    supermercado = models.CharField(max_length = 400, null=True, blank = True, verbose_name = 'Supermercado')
    image = models.ImageField(upload_to="images/", null=True, blank = True)
    description = models.CharField(max_length = 5000, null=True, blank = True, verbose_name = 'Description')
