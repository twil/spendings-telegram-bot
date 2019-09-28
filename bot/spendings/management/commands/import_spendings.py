import csv
from django.core.management.base import BaseCommand, CommandError
from bot.spendings.models import Spending, Label

class Command(BaseCommand):
    help = 'Import spendings from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument(
            'file',
            type=str,
            help='a CSV file with spendings. should contain following columns: date,ammount,[currency],[labels],[owner]'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('TODO:'))
