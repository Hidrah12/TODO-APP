# Generated by Django 4.0.5 on 2022-08-18 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='difficulty',
        ),
        migrations.DeleteModel(
            name='DifficultyTask',
        ),
    ]
