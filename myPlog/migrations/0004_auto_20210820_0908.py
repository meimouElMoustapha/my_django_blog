# Generated by Django 3.2.5 on 2021-08-20 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPlog', '0003_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created',
        ),
        migrations.AddField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]