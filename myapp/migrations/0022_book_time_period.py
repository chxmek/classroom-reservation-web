# Generated by Django 5.0.2 on 2024-03-26 06:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='time_period',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
