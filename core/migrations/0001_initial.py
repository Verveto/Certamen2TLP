# Generated by Django 5.0.6 on 2024-06-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('estudiante', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('tema', models.CharField(choices=[('0', 'Software'), ('1', 'Hardware'), ('2', 'Tesis'), ('3', 'Pyme')], max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('profesor', models.CharField(max_length=100)),
            ],
        ),
    ]
