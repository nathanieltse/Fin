# Generated by Django 3.1.7 on 2021-04-29 05:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0003_auto_20210426_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='spending',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
