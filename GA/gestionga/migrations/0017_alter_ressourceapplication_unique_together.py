# Generated by Django 4.2.5 on 2023-12-17 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionga', '0016_ressourceapplication'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ressourceapplication',
            unique_together={('ressource', 'application')},
        ),
    ]
