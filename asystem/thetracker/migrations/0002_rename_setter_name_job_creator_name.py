# Generated by Django 4.0.5 on 2022-07-12 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thetracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='setter_name',
            new_name='creator_name',
        ),
    ]
