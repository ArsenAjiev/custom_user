# Generated by Django 4.0 on 2022-09-13 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
        ('dealers', '0003_rename_cars_dealerprofile_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealerprofile',
            name='car',
            field=models.ManyToManyField(through='dealers.DealerCar', to='cars.Car'),
        ),
    ]
