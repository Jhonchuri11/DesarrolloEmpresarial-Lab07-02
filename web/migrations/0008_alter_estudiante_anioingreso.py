# Generated by Django 3.2 on 2023-10-18 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20231018_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='anioingreso',
            field=models.DateField(),
        ),
    ]
