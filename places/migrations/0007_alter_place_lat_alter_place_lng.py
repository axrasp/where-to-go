# Generated by Django 4.1 on 2022-09-02 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.CharField(max_length=20, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.CharField(max_length=20, verbose_name='Долгота'),
        ),
    ]