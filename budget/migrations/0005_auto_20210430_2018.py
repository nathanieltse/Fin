# Generated by Django 3.1.7 on 2021-04-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_spending_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='recived',
        ),
        migrations.AddField(
            model_name='transfer',
            name='received',
            field=models.BooleanField(default=False),
        ),
    ]
