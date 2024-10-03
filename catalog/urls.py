from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import *

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products_detail'),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path("contacts/", contacts, name="contact"),
    path("category/", CategoryListView.as_view(), name="category_list"),
]