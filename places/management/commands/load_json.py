import requests
import json
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


def load_json(json_path: str, url=False):
    if url:
        response = requests.get(json_path)
        response.raise_for_status()
        places = response.json()
    else:
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
            Image.objects.create(
                place=new_place,
                number=indx,
                image=ContentFile(image.content)
            )


class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['url']:
            load_json(options['url'], url=True)
        load_json(options['path'])


    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            action='store',
            help='Импорт локаций в формате JSON (локальный путь). '
                 'Пример: python3 manage.py -j your_json_path'
        )

        parser.add_argument(
            '-u',
            '--url',
            action='store',
            help='Импорт локаций в формате JSON (URL). '
                 'Пример: python3 manage.py -u http://your-url.com'
        )
