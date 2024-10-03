from django.db import models, connection

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(
                f"TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE"
            )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="products/photo",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите название категории продукта",
        related_name="products",
        **NULLABLE,
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку",
        help_text="Введите цену за покупку продукта"
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
        null=False,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        blank=True,
        null=True,
        help_text="Укажите дату последнего изменения",
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0

    )
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано'
    )
    slug = models.CharField(
        max_length=150,
        verbose_name='slug',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Наименование продукта",
        related_name="version",
        on_delete=models.SET_NULL,
        **NULLABLE,
    )
    version_number = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии продукта",
        help_text="Введите номер версии продукта",
        **NULLABLE,
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Наименование версии продукта",
        help_text="Введите наименование версии продукта",
        **NULLABLE,
    )
    version_sign = models.BooleanField(
        verbose_name="признак текущей версии", help_text="Версия активна?", default=True
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["product", "version_number", "version_name"]

    def __str__(self):
        return self.version_name
