# Generated by Django 2.1.2 on 2018-10-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_career'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]