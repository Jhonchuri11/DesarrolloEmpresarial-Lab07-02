# Generated by Django 3.2 on 2023-10-18 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_matriculau_matricula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='anioacademico',
            field=models.DateTimeField(verbose_name='Año academico'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='fecha',
            field=models.DateTimeField(verbose_name='Fecha de matricula'),
        ),
    ]
