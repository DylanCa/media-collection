# Generated by Django 4.0.1 on 2022-02-09 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0006_added_cover_path_to_episodes_and_shows'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='season',
            unique_together={('show', 'season_number')},
        ),
    ]