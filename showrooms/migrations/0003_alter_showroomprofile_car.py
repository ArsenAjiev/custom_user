# Generated by Django 4.0 on 2022-09-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('showrooms', '0002_rename_cars_showroomprofile_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroomprofile',
            name='car',
            field=models.ManyToManyField(through='showrooms.ShowroomCar', to='cars.Car'),
        ),
    ]
