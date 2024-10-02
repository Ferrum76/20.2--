from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import Product


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_products = Product.objects.order_by('-created_at')[:5]
        print(latest_products)  # Вывод в консоль
        context['latest_products'] = latest_products
        return context


def products_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)
