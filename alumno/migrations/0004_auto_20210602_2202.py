# Generated by Django 3.1.5 on 2021-06-03 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0003_comentario_alumno'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='comentario',
            name='texto',
            field=models.TextField(blank=True),
        ),
    ]
