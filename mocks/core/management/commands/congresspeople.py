import os
from csv import DictReader

from django.core.management import BaseCommand

from mocks.core.models import Congressperson


class Command(BaseCommand):

    def add_arguments(self, parser, add_drop_all=True):
        parser.add_argument('source', help='Path to the .csv dataset')

    def handle(*args, **options):
        source = options.get('source')
        if not os.path.exists(source):
            raise FileNotFoundError(os.path.abspath(source))

        print('Reading dataset…')
        count = 0
        with open(source) as csv_file:
            reader = DictReader(csv_file)
            for row in reader:
                Congressperson.objects.create(**row)
                count += 1
                print(f'{count} congresspeople imported…', end='\r')

        print()
        print('Done!')
