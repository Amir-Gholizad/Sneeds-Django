# Generated by Django 2.0.5 on 2018-10-17 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_useruploadedbooklet_booklet_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='useruploadedbooklet',
            name='status',
            field=models.CharField(blank=True, choices=[('s', 'مشاهده شد'), ('p', 'در حال انجام'), ('f', 'آپلود شد'), ('c', 'لغو شد')], default='s', help_text='وضعیت دانلود و آپلود جزوه اصلی', max_length=1),
        ),
    ]