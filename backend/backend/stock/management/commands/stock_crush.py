from django.core.management.base import BaseCommand

from stock.models import StockMoveModel


class Command(BaseCommand):
    help = 'Erase all the stock.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Crushing moves...'))
        self.crush_moves()
        self.stdout.write(self.style.SUCCESS(
            'Moves crushed successfully!'))

    def crush_moves(self):
        StockMoveModel.objects.all().delete()
