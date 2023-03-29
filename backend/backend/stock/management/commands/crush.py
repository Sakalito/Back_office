from django.core.management.base import BaseCommand

from product.models import ProductModel


class Command(BaseCommand):
    help = 'Erase product list.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Crushing products...'))
        self.crush_products()
        self.stdout.write(self.style.SUCCESS(
            'Products crushed successfully!'))

    def crush_products(self):
        ProductModel.objects.all().delete()
