# Generated by Django 3.2 on 2023-10-14 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TblAlumno',
            fields=[
                ('alumno_id', models.AutoField(primary_key=True, serialize=False)),
                ('alumno_nombre', models.CharField(max_length=100)),
                ('alumno_email', models.CharField(max_length=100)),
            ],
        ),
    ]
