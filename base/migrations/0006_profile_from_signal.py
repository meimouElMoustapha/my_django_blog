# Generated by Django 3.2.5 on 2021-08-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20210816_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='from_signal',
            field=models.BooleanField(default=False),
        ),
    ]
