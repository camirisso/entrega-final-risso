# Generated by Django 4.0.3 on 2022-03-24 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EstudioApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='enviada',
        ),
    ]
