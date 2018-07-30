# Generated by Django 2.0.6 on 2018-07-20 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0012_test_test_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestFillInAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25)),
                ('position', models.PositiveSmallIntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test')),
            ],
        ),
        migrations.CreateModel(
            name='TestFillInText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test')),
            ],
        ),
        migrations.DeleteModel(
            name='TestFillIn',
        ),
    ]
