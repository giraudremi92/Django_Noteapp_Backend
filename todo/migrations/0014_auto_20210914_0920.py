# Generated by Django 3.2.6 on 2021-09-14 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0013_remove_todo_duedate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoList',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='couleur',
            new_name='color',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='titre',
            new_name='title',
        ),
    ]
