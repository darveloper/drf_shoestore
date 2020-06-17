from django.core.management.base import BaseCommand, CommandError
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe

class Command(BaseCommand):
    def handle(self, *args, **options):
        types = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other'
        ]
        colors = [
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'indigo',
            'violet',
            'white',
            'black'
        ]
        try:
            for type in types:
                ShoeType.objects.create(style=type)
            for color in colors:
                ShoeColor.objects.create(color_name=color)
            print("Data Populated")
        except:
            raise CommandError("Something broke.")
