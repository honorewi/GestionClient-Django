# Generated by Django 5.1 on 2024-08-14 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produits',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 8, 14, 10, 0)),
            preserve_default=False,
        ),
    ]
