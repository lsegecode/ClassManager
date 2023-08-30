# Generated by Django 4.2.2 on 2023-08-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='copiaDNI_A',
            field=models.ImageField(blank=True, upload_to='alumnado/images/'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='direccion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='tutores',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
