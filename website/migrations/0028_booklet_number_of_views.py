# Generated by Django 2.0.5 on 2018-10-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_auto_20181017_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='number_of_views',
            field=models.IntegerField(default=0, editable=False, verbose_name='تعداد مشاهده'),
        ),
    ]