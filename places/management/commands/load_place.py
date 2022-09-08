import requests
import json
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.core.exceptions import MultipleObjectsReturned

from places.models import Image, Place


def load_place(json_path: str, url=False):
    if url:
        response = requests.get(json_path)
        response.raise_for_status()
        places = response.json()
    else:
        with open(json_path, 'r') as f:
            places = json.load(f)

    for place in places['places']:
        try:
            import_place, _ = Place.objects.get_or_create(
                title=place['title'],
                lng=place['coordinates']['lng'],
                lat=place['coordinates']['lat'],
                defaults={
                    'description_long': place.get('description_long', ''),
                    'description_short': place.get('description_short', ''),
                },
            )

            for index, image_url in enumerate(place['imgs'], start=1):
                image = requests.get(image_url)
                image.raise_for_status()
                Image.objects.create(
                    place=import_place,
                    number=index,
                    image=ContentFile(image.content, name=f'{place["title"]}_{index}.jpg')
                )

        except MultipleObjectsReturned as e:
            print(e)
            continue

class Command(BaseCommand):
    def handle(self, *args, **options):
        if options['url']:
            load_place(options['url'], url=True)
        load_place(options['path'])

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
