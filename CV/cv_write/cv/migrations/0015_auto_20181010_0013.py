# Generated by Django 2.1.2 on 2018-10-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0014_auto_20181009_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='profive',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='profour',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='proone',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='prothree',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='protwo',
        ),
        migrations.AlterField(
            model_name='projects',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
