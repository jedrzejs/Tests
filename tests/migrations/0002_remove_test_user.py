# Generated by Django 2.0.6 on 2018-07-12 16:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='user',
        ),
    ]
