from django.shortcuts import render

from twixapp1.models import Product1


def start_page(request):
    return render(request, 'start_page.html')



def product1(request):
    context = {'product1': Product1.objects.all()}
    return render(request, 'product1.html', context=context)


def show_product1(request, product1_id):
    context = {'products1': Product1.objects.get(pk=product1_id)}
    return render(request, 'result1.html', context=context)
