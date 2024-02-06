# Generated by Django 4.2.5 on 2023-11-01 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionga', '0002_alter_programme_description_programme_habilitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilitation',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilitations', to='gestionga.domaine'),
        ),
        migrations.AlterField(
            model_name='habilitation',
            name='droit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilitations', to='gestionga.droit'),
        ),
        migrations.AlterField(
            model_name='habilitation',
            name='profil',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilitations', to='gestionga.profil'),
        ),
        migrations.AlterField(
            model_name='habilitation',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='habilitations', to='gestionga.programme'),
        ),
    ]
