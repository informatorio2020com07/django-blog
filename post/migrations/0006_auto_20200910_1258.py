# Generated by Django 3.1 on 2020-09-10 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200909_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='estado',
            field=models.CharField(choices=[('public', 'Publico'), ('hidden', 'Oculto')], default='public', max_length=6),
        ),
        migrations.AlterField(
            model_name='calificacionpost',
            name='calificacion',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(-5)]),
        ),
    ]
