# Generated by Django 3.2.2 on 2021-05-18 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tatuador',
            fields=[
                ('idTatuador', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID del tatuador')),
                ('nombreTatuador', models.CharField(max_length=50, verbose_name='Nombre del tatuador')),
                ('estiloTatuador', models.CharField(max_length=50, verbose_name='Estilo del tauador')),
            ],
        ),
        migrations.CreateModel(
            name='Diseño',
            fields=[
                ('idDiseño', models.IntegerField(max_length=7, primary_key=True, serialize=False, verbose_name='ID del diseño')),
                ('nombreDiseño', models.CharField(max_length=20, verbose_name='Nombre del Diseño')),
                ('categoria', models.CharField(max_length=20, verbose_name='Categoria del diseño')),
                ('tatuador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tatuador')),
            ],
        ),
    ]
