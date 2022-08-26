from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length=200,
        blank=False,
    )
    description_short = models.TextField(
        'Краткое описание',
        blank=True
    )
    description_long = models.TextField(
        'Полное описание html',
        blank=True
    )
    lng = models.CharField(
        'Долгота',
        max_length=20,
        blank=True
    )
    ltd = models.CharField(
        'Широта',
        max_length=20,
        blank=True
    )

    def __str__(self):
        return str(self.title)