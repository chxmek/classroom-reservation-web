# Generated by Django 5.0.2 on 2024-03-25 09:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_book_image_remove_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.ImageField(default=datetime.datetime(2024, 3, 25, 9, 27, 57, 377797, tzinfo=datetime.timezone.utc), upload_to='img/'),
            preserve_default=False,
        ),
    ]
