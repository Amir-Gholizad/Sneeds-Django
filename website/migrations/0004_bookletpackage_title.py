# Generated by Django 2.0.5 on 2018-10-22 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_bookletpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookletpackage',
            name='title',
            field=models.CharField(default='', max_length=120),
        ),
    ]
