# Generated by Django 5.0.1 on 2024-01-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0009_alter_card_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='signature',
            field=models.ImageField(max_length=500, upload_to='signature/'),
        ),
    ]
