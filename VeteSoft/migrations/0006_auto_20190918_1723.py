# Generated by Django 2.1 on 2019-09-18 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VeteSoft', '0005_auto_20190918_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examen',
            name='Nombre',
        ),
        migrations.AlterField(
            model_name='detallecita',
            name='Observacion',
            field=models.CharField(max_length=500),
        ),
    ]