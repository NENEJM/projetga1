# Generated by Django 4.2.5 on 2023-12-16 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionga', '0015_dictionnaire_sgbe_sgbf_sgcam_sgci_sgcongo_sgm_sgsn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RessourceApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionga.application')),
                ('ressource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionga.ressource')),
            ],
        ),
    ]
