# Generated by Django 2.0.6 on 2018-07-12 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('tests', '0005_test_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Test')),
            ],
        ),
        migrations.RemoveField(
            model_name='testabc',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='testtruefalse',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='testwriteanswer',
            name='answer',
        ),
        migrations.AlterField(
            model_name='student',
            name='tests',
            field=models.ManyToManyField(to='tests.Answer'),
        ),
    ]
