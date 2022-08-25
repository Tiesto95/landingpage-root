from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.
def first_page(request):
    obj = Order.objects.all()
    form = OrderForm()
    title = 'Главная страница'
    return render(request, './index.html', {'object_list': obj, 'form': form, 'title': title})

def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    elements = Order(order_name = name, order_phone = phone)
    elements.save()
    return render(request, './thanks_page.html', {'name': name, 'phone': phone})
