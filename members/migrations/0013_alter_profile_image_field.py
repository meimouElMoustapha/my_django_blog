# Generated by Django 3.2.5 on 2021-08-20 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_alter_profile_image_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_field',
            field=models.ImageField(default='media/computer.png', upload_to='media/'),
        ),
    ]
