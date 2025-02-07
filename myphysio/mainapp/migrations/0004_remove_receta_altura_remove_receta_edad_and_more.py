# Generated by Django 5.1.2 on 2024-11-18 05:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receta',
            name='altura',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='receta',
            name='peso',
        ),
        migrations.AlterField(
            model_name='receta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.paciente'),
        ),
    ]
