from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse

# Create your views here.
from trades.models import Category, Product, Basket


def index(request):
    return render(request, 'trades/index.html')


def categories(request):
    categories = Category.objects.all()
    return render(request, 'trades/products.html', {'categories': categories})


def by_category(request, category_id, page):
    category = Category.objects.get(id=category_id)
    products_by_category = Product.objects.filter(category=category)
    per_page = 1
    paginator = Paginator(products_by_category, per_page)
    products_paginator = paginator.page(page)

    context = {'products': products_paginator, 'category': category}
    return render(request, 'trades/products_to_buy.html', context)


def basket(request):
    user_basket = Basket.objects.filter(user=request.user)
    context = {'baskets': user_basket}
    return render(request, 'trades/basket.html', context)


def basket1(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.last()
        baskets.quantity += 1
        baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_min(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    baskets = baskets.last()
    if baskets.quantity > 1:
        baskets.quantity -= 1
        baskets.save()
    else:
        baskets.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
