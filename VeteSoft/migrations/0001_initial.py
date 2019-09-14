# Generated by Django 2.1 on 2019-09-14 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Documento', models.CharField(max_length=45)),
                ('Nombres', models.CharField(max_length=45)),
                ('PrimerApellido', models.CharField(max_length=45)),
                ('SegundoApellido', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('Celular', models.CharField(max_length=45)),
                ('Direccion', models.CharField(max_length=45)),
                ('FechaRegistro', models.DateField(auto_now_add=True, null=True)),
                ('Estado', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CentroVeterinario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('Direccion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Documento', models.CharField(max_length=45)),
                ('Nombres', models.CharField(max_length=45)),
                ('PrimerApellido', models.CharField(max_length=45)),
                ('SegundoApellido', models.CharField(max_length=45, null=True)),
                ('FechaNacimiento', models.DateField()),
                ('Celular', models.CharField(max_length=45)),
                ('Direccion', models.CharField(max_length=45)),
                ('FechaRegistro', models.DateField(auto_now_add=True, null=True)),
                ('Estado', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Observacion', models.CharField(max_length=50)),
                ('Citas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Citas')),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ExamenMascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Examen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Examen')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Codigo', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('Genero', models.CharField(default='', max_length=45)),
                ('Cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Cliente')),
                ('HistoriaClinica', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.HistoriaClinica')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Documento', models.CharField(max_length=45)),
                ('Nombres', models.CharField(max_length=45)),
                ('PrimerApellido', models.CharField(max_length=45)),
                ('SegundoApellido', models.CharField(max_length=45)),
                ('FechaNacimiento', models.DateField()),
                ('Celular', models.CharField(max_length=45)),
                ('Direccion', models.CharField(max_length=45)),
                ('FechaRegistro', models.DateField(auto_now_add=True, null=True)),
                ('Estado', models.BooleanField(default=True, null=True)),
                ('Genero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Genero')),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='ResultadoClinico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Resultado', models.CharField(max_length=45)),
                ('ExamenMascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.ExamenMascota')),
            ],
        ),
        migrations.AddField(
            model_name='mascotas',
            name='Raza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Raza'),
        ),
        migrations.AddField(
            model_name='detallecita',
            name='ExamenMascota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.ExamenMascota'),
        ),
        migrations.AddField(
            model_name='detallecita',
            name='Medicamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Medicamento'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='Genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Genero'),
        ),
        migrations.AddField(
            model_name='citas',
            name='Mascotas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Mascotas'),
        ),
        migrations.AddField(
            model_name='citas',
            name='Medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Medico'),
        ),
        migrations.AddField(
            model_name='administrador',
            name='Genero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VeteSoft.Genero'),
        ),
    ]
