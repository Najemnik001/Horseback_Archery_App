# Generated by Django 3.2.6 on 2021-08-23 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HArcherApp', '0004_auto_20210823_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='horse',
            field=models.CharField(default='Koń', max_length=64),
        ),
    ]
