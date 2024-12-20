# Generated by Django 5.1.1 on 2024-12-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_reporte_horanconsulta'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='act_causante',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='act_fisica',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='alimentacion',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_materno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_paterno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='condicion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='descanso',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='descripcion_dolor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='direccion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='frecuencia_dolor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='intensidad_dolor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='lesiones',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='medicacion_actual',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='presion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sintomas',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefonoP',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tratamiento',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tratamientos_previos',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='compromisos',
            field=models.TextField(max_length=555),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='descripcion',
            field=models.TextField(max_length=555),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='motivoconsulta',
            field=models.TextField(max_length=555),
        ),
        migrations.AlterUniqueTogether(
            name='citas',
            unique_together={('paciente', 'fecha', 'hora')},
        ),
    ]
