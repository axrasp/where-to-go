import requests
import json
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


def load_json(json_path: str):
    try:
        response = requests.get(json_path)
        response.raise_for_status()
        places = response.json()
    except requests.exceptions.MissingSchema:
        with open(json_path, 'r') as plcs:
            places = json.load(plcs)

    for place in places['places']:
        new_place, _ = Place.objects.get_or_create(
            title=place['title'],
            defaults={
                'description_long': place['description_long'],
                'description_short': place['description_short'],
                'lng': place['coordinates']['lng'],
                'lat': place['coordinates']['lat'],
            },
        )
        for indx, image_url in enumerate(place['imgs'], start=1):
            image = requests.get(image_url)
            image.raise_for_status()
            new_image = Image.objects.create(place=new_place, number=indx)
            new_image.image.save(
                f'{new_place.title}_{indx}.jpg', ContentFile(image.content), save=True
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        load_json(options['json'])

    def add_arguments(self, parser):
        parser.add_argument(
            '-j',
            '--json',
            action='store',
            help='Импорт локаций в формат JSON (URL или путь). '
                 'Пример: python3 manage.py -j your_json_path'
        )
