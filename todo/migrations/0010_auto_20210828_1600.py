# Generated by Django 3.2.6 on 2021-08-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_alter_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='coordx',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='todo',
            name='coordy',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]