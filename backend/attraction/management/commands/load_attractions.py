import json
from django.core.management.base import BaseCommand
from attraction.models import Attraction

class Command(BaseCommand):
    help = 'Load attraction data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = f.read()
                market = Attraction()
                market.load_from_json(json_data)
                self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except UnicodeDecodeError as e:
            self.stderr.write(self.style.ERROR(f"Unicode decode error: {e}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"An error occurred: {e}"))