# Generated by Django 5.0.2 on 2024-03-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_book_time_period'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time_period',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
