from django.core.management.base import BaseCommand
from catalog.models import Category, Product
import json
import os

class Command(BaseCommand):
    help = 'Загружает данные из фикстур и очищает старые данные'

    def handle(self, *args, **options):
        fixture_path = os.path.join('catalog', 'fixtures', 'catalog_data.json')

        if not os.path.exists(fixture_path):
            self.stdout.write(self.style.ERROR(f'Файл фикстуры {fixture_path} не найден.'))
            return

        with open(fixture_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Очистка существующих данных
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Загрузка новых данных
        for entry in data:
            model = entry['model']
            pk = entry['pk']
            fields = entry['fields']

            if model == 'catalog.category':
                Category.objects.create(id=pk, **fields)
            elif model == 'catalog.product':
                category = Category.objects.get(pk=fields['category'])
                Product.objects.create(
                    id=pk,
                    name=fields['name'],
                    description=fields.get('description', ''),
                    image=fields.get('image', ''),
                    category=category,
                    price=fields['price'],
                    created_at=fields.get('created_at', None),
                    updated_at=fields.get('updated_at', None)
                )

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены из фикстур.'))
