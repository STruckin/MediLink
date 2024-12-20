# Generated by Django 5.1.3 on 2024-11-19 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_citas_hora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cuello_d', models.CharField(blank=True, max_length=50, null=True)),
                ('torso_d', models.CharField(blank=True, max_length=50, null=True)),
                ('m_sup_d', models.CharField(blank=True, max_length=50, null=True)),
                ('m_inf_d', models.CharField(blank=True, max_length=50, null=True)),
                ('cuello_i', models.CharField(blank=True, max_length=50, null=True)),
                ('torso_i', models.CharField(blank=True, max_length=50, null=True)),
                ('m_sup_i', models.CharField(blank=True, max_length=50, null=True)),
                ('m_inf_i', models.CharField(blank=True, max_length=50, null=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.paciente')),
            ],
        ),
    ]
