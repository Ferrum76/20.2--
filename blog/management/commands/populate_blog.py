from django.core.management.base import BaseCommand
from blog.models import Blog
import json

class Command(BaseCommand):
    help = 'Загружает данные из фикстур и очищает старые данные'

    @staticmethod
    def json_read_blogs():
        """ "получаем данные из фикстуры с продуктами"""
        with open("=blog/fixtures/blog.json", "r", encoding="utf-8") as f:
            products = json.load(f)
            return products

    def handle(self, *args, **options):
        Blog.objects.all().delete()

        blog_for_create = []

        for blog in Command.json_read_blogs():
            blog_for_create.append(
                Blog(
                    pk=blog["pk"],
                    title=blog["fields"]["title"],
                    slug=blog["fields"]["slug"],
                    body=blog["fields"]["body"],
                    image=blog["fields"]["image"],
                    created_at=blog["fields"]["created_at"],
                    views_count=blog["fields"]["views_count"],
                    is_published=blog["fields"]["is_published"],
                )
            )

        Blog.objects.bulk_create(blog_for_create)
