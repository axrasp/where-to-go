from django.db import models
from tinymce.models import HTMLField


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
    description_long = HTMLField(
        'Полное описание',
        blank=True
    )
    lng = models.CharField(
        'Долгота',
        max_length=20,
        blank=True
    )
    lat = models.CharField(
        'Широта',
        max_length=20,
        blank=True
    )

    def __str__(self):
        return str(self.title)


class Image (models.Model):
    number = models.IntegerField(
        'Номер картинки',
    )
    image = models.ImageField(
        'Картинка',
        blank=False,
        null=False
    )
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name='Место',
        related_name='imgs'
    )

    def __str__(self):
        return f"{str(self.number)} {str(self.place)}"

    class Meta:
        ordering = ["number"]
