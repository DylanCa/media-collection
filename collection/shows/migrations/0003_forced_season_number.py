# Generated by Django 4.0.1 on 2022-02-08 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0002_added_season_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='season_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
