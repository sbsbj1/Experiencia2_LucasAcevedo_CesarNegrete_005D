# Generated by Django 4.0.4 on 2022-06-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petsy', '0002_accesorio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesorio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
