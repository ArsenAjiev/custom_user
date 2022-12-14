# Generated by Django 4.0 on 2022-09-13 16:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        ('dealers', '0004_alter_dealerprofile_car'),
        ('showrooms', '0003_alter_showroomprofile_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowroomSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('discount', models.DecimalField(decimal_places=2, default=0.01, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('showroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showrooms.showroomprofile')),
            ],
        ),
        migrations.CreateModel(
            name='DealerSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('discount', models.DecimalField(decimal_places=2, default=0.01, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dealers.dealerprofile')),
            ],
        ),
    ]
