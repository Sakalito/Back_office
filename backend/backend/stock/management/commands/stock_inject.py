from django.core.management.base import BaseCommand

from stock.serializers import StockMoveSerializer

import json


class Command(BaseCommand):
    help = 'Inject predefined Stock Moves.'

    file_path = 'stock/management/commands/medium.json'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Injecting Moves...'))
        self.inject_moves()
        self.stdout.write(self.style.SUCCESS(
            'Products injected successfully!'))

    def fetch_moves(self) -> list:
        with open(self.file_path, 'r') as file:
            return json.load(file)

    # offset due to products injection tests
    product_id_offset = 17

    def format_items(self, item: dict) -> dict:
        return {
            'product': item.get('pid') + self.product_id_offset,
            'amount': item.get('amount'),
        }

    def format_move(self, move: dict) -> dict:
        items = move.pop('products')
        move['products'] = [self.format_items(item) for item in items]
        return move

    def inject_moves(self):
        moves = self.fetch_moves()
        for move in moves:
            serializer = StockMoveSerializer(data=self.format_move(move))
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS('Move injected !'))
            else:
                self.stdout.write(self.style.ERROR(
                    f'Error while injecting move: {move}'))
                self.stdout.write(self.style.ERROR(
                    f'Error: {serializer.errors}'))
