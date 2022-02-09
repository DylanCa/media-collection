# Generated by Django 4.0.1 on 2022-02-09 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_add_has_liked_to_media_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediastatusperuser',
            name='status',
            field=models.CharField(choices=[('watched', 'watched'), ('read', 'read'), ('ongoing', 'ongoing'), ('played', 'played')], default='ongoing', max_length=10),
        ),
    ]
