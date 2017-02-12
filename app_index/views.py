from django.shortcuts import render
from .models import *
# Create your views here.


def indexView(request):

    context = {}

    return render(request, "index.html", context)


def productsView(request):

    customer = Customer.objects.get(pk=1)
    products = Product.objects.all()

    print(customer.name)
    context = {
        "customer": customer,
        "products": products,
    }



    return render(request, "products.html", context)