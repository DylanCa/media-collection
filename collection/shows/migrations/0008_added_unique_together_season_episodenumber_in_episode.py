# Generated by Django 4.0.1 on 2022-02-09 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0007_added_unique_together_show_seasonnumber_in_season'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='episode',
            unique_together={('season', 'episode_number')},
        ),
    ]
