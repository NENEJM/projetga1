# Generated by Django 4.2.5 on 2023-10-30 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_domaine', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Droit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_droit', models.CharField(max_length=100)),
                ('symbole_droit', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_profil', models.CharField(max_length=100)),
                ('description_profil', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_programme', models.CharField(max_length=100)),
                ('description_programme', models.TextField()),
                ('domaine_programme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programme_domaine', to='gestionga.domaine')),
            ],
        ),
    ]
