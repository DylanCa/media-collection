# Generated by Django 4.0.1 on 2022-02-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_added_played_to_mediastatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediastatusperuser',
            name='has_liked',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
