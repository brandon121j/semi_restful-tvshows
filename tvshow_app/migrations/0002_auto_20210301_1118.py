# Generated by Django 2.2.4 on 2021-03-01 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(),
        ),
    ]
