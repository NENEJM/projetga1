# Generated by Django 4.2.5 on 2023-11-08 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionga', '0009_remove_ressource_numero_ip_ressource_poste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ressource',
            name='poste',
        ),
        migrations.AddField(
            model_name='ressource',
            name='matricule',
            field=models.CharField(default='95XJ', max_length=20),
        ),
        migrations.AddField(
            model_name='ressource',
            name='numero_ip',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
