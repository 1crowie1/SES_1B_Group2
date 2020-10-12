# Generated by Django 3.1 on 2020-10-12 12:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('number_of_people', models.IntegerField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300, null=True)),
                ('cost', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.CharField(max_length=60, null=True)),
                ('date_created', models.DateField(null=True)),
                ('last_edited', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('open_hours', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=60, null=True)),
                ('date_created', models.DateField(default=datetime.date(2020, 10, 12))),
                ('valid_until', models.DateField(null=True)),
                ('points_percent', models.IntegerField(null=True)),
                ('is_valid', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('tax_file_number', models.IntegerField()),
                ('date_hired', models.DateField(null=True)),
                ('is_manager', models.BooleanField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='staff', to='api.restaurant')),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.meal')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('meal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='api.meal')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='meals', to='api.menu')),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Rewards',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('reward', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customers', to='api.reward')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='rewards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('payment_details', models.CharField(max_length=200, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Order',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='api.booking')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='api.order')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='api.restaurant'),
        ),
    ]
