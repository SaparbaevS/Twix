from django.shortcuts import render

from twixapp2.models import Product2


def start_page(request):
    return render(request, 'start_page.html')

def product2(request):
    context = {'product2': Product2.objects.all()}
    return render(request, 'product2.html', context=context)

def show_product2(request, product2_id):
    context = {'products2': Product2.objects.get(pk=product2_id)}
    return render(request, 'result2.html', context=context)