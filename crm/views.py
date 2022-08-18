from django.shortcuts import render
from .models import Order


# Create your views here.
def first_page(request):
    obj = Order.objects.all()
    return render(request, './index.html', {'object_list': obj})
