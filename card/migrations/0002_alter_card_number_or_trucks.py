# Generated by Django 5.0.1 on 2024-01-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='number_or_trucks',
            field=models.IntegerField(default=0),
        ),
    ]
