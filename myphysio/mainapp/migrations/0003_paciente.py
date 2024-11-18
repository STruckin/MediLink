# Generated by Django 5.1.2 on 2024-11-17 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_rename_recetas_receta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('telefonoP', models.IntegerField()),
                ('emailP', models.EmailField(max_length=254)),
                ('sintomas', models.CharField(max_length=50)),
                ('frecuencia_dolor', models.CharField(max_length=50)),
                ('act_causante', models.CharField(max_length=50)),
                ('descripcion_dolor', models.CharField(max_length=50)),
                ('intensidad_dolor', models.CharField(max_length=50)),
                ('tratamiento', models.CharField(max_length=50)),
                ('lesiones', models.CharField(max_length=50)),
                ('condicion', models.CharField(max_length=50)),
                ('tratamientos_previos', models.CharField(max_length=50)),
                ('medicacion_actual', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('rango_mov', models.IntegerField()),
                ('presion', models.CharField(max_length=50)),
                ('ocupacion', models.CharField(max_length=50)),
                ('act_fisica', models.CharField(max_length=50)),
                ('descanso', models.CharField(max_length=50)),
                ('alimentacion', models.CharField(max_length=50)),
            ],
        ),
    ]
