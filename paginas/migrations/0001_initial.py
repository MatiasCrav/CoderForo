# Generated by Django 4.0 on 2022-05-10 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('tema', models.CharField(max_length=255)),
                ('contenido', models.TextField()),
                ('comision', models.IntegerField()),
                ('posteador', models.CharField(max_length=255)),
            ],
        ),
    ]
