# Generated by Django 5.1.2 on 2024-11-23 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_historial_pres_atax_historial_pres_ayud_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnostico', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('motivoconsulta', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('compromisos', models.CharField(max_length=255)),
                ('fechasnconsulta', models.DateField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.paciente')),
            ],
        ),
    ]