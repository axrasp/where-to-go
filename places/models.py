from django.db import models
from tinymce.models import HTMLField
from django.db.models import UniqueConstraint
from django.core.validators import MinValueValidator, MaxValueValidator


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
        validators=[
            MaxValueValidator(-180),
            MinValueValidator(180)
        ]

    )
    lat = models.FloatField(
        'Широта',
        validators=[
            MaxValueValidator(-90),
            MinValueValidator(90)
        ]
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['title', 'lat','lng'],
                name='unique_place',
            )
        ]

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
