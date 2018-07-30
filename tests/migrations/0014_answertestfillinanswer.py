# Generated by Django 2.0.6 on 2018-07-26 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0013_auto_20180720_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTestFillInAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25)),
                ('position', models.PositiveSmallIntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Answer')),
            ],
        ),
    ]
