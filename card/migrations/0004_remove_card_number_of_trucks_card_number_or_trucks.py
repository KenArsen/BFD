# Generated by Django 5.0.1 on 2024-01-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_rename_number_or_trucks_card_number_of_trucks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='number_of_trucks',
        ),
        migrations.AddField(
            model_name='card',
            name='number_or_trucks',
            field=models.IntegerField(default=0),
        ),
    ]