# Generated by Django 5.1.2 on 2024-11-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_remove_receta_altura_remove_receta_edad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='presion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
