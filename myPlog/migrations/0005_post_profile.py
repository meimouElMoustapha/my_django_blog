# Generated by Django 3.2.5 on 2021-08-20 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_remove_profile_post'),
        ('myPlog', '0004_auto_20210820_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='members.profile'),
        ),
    ]
