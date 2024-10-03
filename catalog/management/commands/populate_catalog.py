from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
import os

class Command(BaseCommand):
    help = 'Загружает данные из фикстур и очищает старые данные'

    @staticmethod
    def json_read_categories():
        """получаем данные из фикстуры с категориями"""
        with open("catalog/fixtures/categories.json", "r", encoding="utf-8") as f:
            categories = json.load(f)
            return categories

    @staticmethod
    def json_read_products():
        """ "получаем данные из фикстуры с продуктами"""
        with open("catalog/fixtures/products.json", "r", encoding="utf-8") as f:
            products = json.load(f)
            return products

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        Category.truncate_table_restart_id()

        category_for_create = []
        product_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(
                    pk=category["pk"],
                    name=category["fields"]["name"],
                    description=category["fields"]["description"],
                )
            )

        for product in Command.json_read_products():
            print(product)
            product_for_create.append(
                Product(
                    pk=product["pk"],
                    name=product["fields"]["name"],
                    description=product["fields"]["description"],
                    image=product["fields"]["image"],
                    category=Category(pk=category["pk"]),
                    price=product["fields"]["price"],
                    created_at=product["fields"]["created_at"],
                    updated_at=product["fields"]["updated_at"],
                )
            )

        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
