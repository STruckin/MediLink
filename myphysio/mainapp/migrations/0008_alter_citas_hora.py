# Generated by Django 5.1.2 on 2024-11-18 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_paciente_act_causante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='hora',
            field=models.TimeField(),
        ),
    ]