# Generated by Django 5.1.2 on 2024-11-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_paciente_presion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='presion',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
