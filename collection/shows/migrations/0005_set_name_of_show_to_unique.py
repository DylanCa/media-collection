# Generated by Django 4.0.1 on 2022-02-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0004_added_name_description_to_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
