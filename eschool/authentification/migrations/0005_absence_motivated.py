# Generated by Django 3.1.6 on 2021-02-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0004_auto_20210221_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='motivated',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
