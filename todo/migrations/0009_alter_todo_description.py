# Generated by Django 3.2.6 on 2021-08-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_todo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
