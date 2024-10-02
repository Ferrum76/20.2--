from django.urls import path

import catalog.views as catalog_views

app_name = 'catalog'

urlpatterns = [
    path('', catalog_views.HomeView.as_view(), name='home'),
    path('products/', catalog_views.products_list, name='products_list'),
    path('products/<int:pk>/', catalog_views.product_detail, name='product_detail'),
]
