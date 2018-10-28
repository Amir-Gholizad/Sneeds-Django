# Generated by Django 2.0.5 on 2018-10-27 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('discounts', '0003_auto_20181026_1949'),
    ]

    operations = [
        migrations.CreateModel(
            name='CafeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cafe', to='discounts.Cafe')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
