from django.shortcuts import render
from .models import Order


# Create your views here.
def first_page(request):
    obj = Order.objects.all()
    return render(request, './index.html', {'object_list': obj})

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    elements = Order(order_name = name, order_phone = phone)
    elements.save()
    return render(request, './thanks_page.html', {'name': name, 'phone': phone})
