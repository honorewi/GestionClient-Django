# Generated by Django 5.1 on 2024-08-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_tag_produits_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='produits',
            name='categorie',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
