# Generated by Django 4.1 on 2022-08-31 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_image_place'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='ltd',
            new_name='lat',
        ),
    ]
