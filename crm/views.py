from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlaider
from price.models import PriceCard, PriceTable
from telebot.tgSendMesage import Send_Message


# Create your views here.
def first_page(request):
    sliders = CmsSlaider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
        'sliders': sliders,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form
    }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    Send_Message(name, phone)
    elements = Order(order_name = name, order_phone = phone)
    elements.save()
    return render(request, './thanks.html', {'name': name})
