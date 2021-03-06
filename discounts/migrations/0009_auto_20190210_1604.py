# Generated by Django 2.1.3 on 2019-02-10 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0008_auto_20190210_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='address',
            field=models.CharField(help_text='In a specific format.', max_length=256),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='phone_number',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
        ),
    ]
