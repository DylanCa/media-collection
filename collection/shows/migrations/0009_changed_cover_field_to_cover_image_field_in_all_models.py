# Generated by Django 4.0.1 on 2022-02-09 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0008_added_unique_together_season_episodenumber_in_episode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='cover',
            new_name='cover_image',
        ),
        migrations.RenameField(
            model_name='season',
            old_name='cover',
            new_name='cover_image',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='cover',
            new_name='cover_image',
        ),
    ]
