# Generated by Django 3.2.5 on 2021-08-18 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='field',
        ),
    ]
