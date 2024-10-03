from django.shortcuts import render, get_object_or_404

from .models import Product


def products_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
