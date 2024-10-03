# Generated by Django 5.1.1 on 2024-10-03 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование категории', max_length=50, verbose_name='Наименование категории')),
                ('description', models.TextField(blank=True, help_text='Введите описание категории', null=True, verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование продукта', max_length=50, verbose_name='Наименование продукта')),
                ('description', models.TextField(blank=True, help_text='Введите описание продукта', null=True, verbose_name='Описание продукта')),
                ('image', models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='products/photo', verbose_name='Изображение продукта')),
                ('price', models.IntegerField(help_text='Введите цену за покупку продукта', verbose_name='Цена за покупку')),
                ('created_at', models.DateField(auto_now_add=True, help_text='Укажите дату создания', verbose_name='Дата создания')),
                ('updated_at', models.DateField(blank=True, help_text='Укажите дату последнего изменения', null=True, verbose_name='Дата последнего изменения')),
                ('views_counter', models.PositiveIntegerField(default=0, help_text='Укажите количество просмотров', verbose_name='Счетчик просмотров')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('category', models.ForeignKey(blank=True, help_text='Введите название категории продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='catalog.category', verbose_name='Категория продукта')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'permissions': [('can_change_description', 'Can change description of product'), ('can_change_category', 'Can change category of product'), ('can_cancel__is_published', 'Can cancel is_published')],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveIntegerField(blank=True, default=0, help_text='Введите номер версии продукта', null=True, verbose_name='Номер версии продукта')),
                ('version_name', models.CharField(blank=True, help_text='Введите наименование версии продукта', max_length=50, null=True, verbose_name='Наименование версии продукта')),
                ('version_sign', models.BooleanField(default=True, help_text='Версия активна?', verbose_name='признак текущей версии')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='version', to='catalog.product', verbose_name='Наименование продукта')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
                'ordering': ['product', 'version_number', 'version_name'],
            },
        ),
    ]
