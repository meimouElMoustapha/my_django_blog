# Generated by Django 3.2.5 on 2021-08-15 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_task_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
