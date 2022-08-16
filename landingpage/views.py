from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    title = 'Главная страница'
    name = 'Беслан'
    return render(request, './index.html', {
        'name' : name,
        'title': title
    })