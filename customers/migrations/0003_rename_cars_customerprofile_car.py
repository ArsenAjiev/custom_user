# Generated by Django 4.1.1 on 2022-09-13 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerprofile',
            old_name='cars',
            new_name='car',
        ),
    ]
