from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=200
    )
    description_short = models.TextField(
        'Краткое описание',
        blank=True
    )
    description_long = HTMLField(
        'Полное описание',
        blank=True
    )
    lng = models.FloatField(
        'Долгота',
        max_length=20,
    )
    lat = models.FloatField(
        'Широта',
        max_length=20,
    )

    def __str__(self):
        return self.title


class Image (models.Model):
    number = models.IntegerField(
        'Номер картинки',
    )
    image = models.ImageField(
        'Картинка',
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='imgs'
    )

    def __str__(self):
        return f'{self.number} {self.place}'

    class Meta:
        ordering = ['number']
