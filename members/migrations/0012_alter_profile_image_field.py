# Generated by Django 3.2.5 on 2021-08-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_alter_profile_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_field',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
