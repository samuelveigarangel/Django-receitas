# Generated by Django 4.0.3 on 2022-03-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pessoas',
            new_name='Pessoa',
        ),
    ]