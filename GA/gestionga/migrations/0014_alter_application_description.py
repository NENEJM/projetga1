# Generated by Django 4.2.5 on 2023-11-14 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionga', '0013_alter_application_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='description',
            field=models.TextField(),
        ),
    ]