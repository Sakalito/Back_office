from django.core.management.base import BaseCommand

from product.serializers import ProduitSerializer

import requests


class Command(BaseCommand):
    help = 'Inject predefined list of products.'

    distant_server_product_end_point = 'http://51.255.166.155:1352/tig/products/'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Injecting products...'))
        self.inject_products()
        self.stdout.write(self.style.SUCCESS(
            'Products injected successfully!'))

    def fetch_products(self) -> list:
        response = requests.get(self.distant_server_product_end_point)
        return response.json()

    def format_product(self, product: dict) -> dict:
        return {
            'name': product.get('name'),
            'comments': product.get('comments'),
            'unit': product.get('unit'),
            'availability': product.get('availability'),
            'price': product.get('price'),
            'owner': 1,  # product.get('owner'),
            'category': product.get('category') + 1,
            'discount': {
                "rate": product.get('discount'),
            } if product.get('discount') else None,
        }

    def inject_products(self):
        products = self.fetch_products()
        for product in products:
            product = self.format_product(product)
            product_serializer = ProduitSerializer(data=product)
            if product_serializer.is_valid():
                product_serializer.save()
                self.stdout.write(self.style.SUCCESS(
                    f'Product injected: {product.get("name")}'))
            else:
                self.stdout.write(self.style.ERROR(
                    f'Error while injecting product: {product}'))
                self.stdout.write(self.style.ERROR(
                    f'Error: {product_serializer.errors}'))
                

