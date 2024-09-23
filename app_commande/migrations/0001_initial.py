# Generated by Django 5.0.7 on 2024-08-07 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=20)),
                ('quantite', models.IntegerField()),
                ('prix_unitaire', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_commande.categorie')),
            ],
        ),
    ]
