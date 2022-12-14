# Generated by Django 4.1 on 2022-08-26 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Полное описание html')),
                ('lng', models.CharField(blank=True, max_length=20, verbose_name='Долгота')),
                ('ltd', models.CharField(blank=True, max_length=20, verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер картинки')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='places.place', verbose_name='Место')),
            ],
        ),
    ]
