# Generated by Django 3.1 on 2020-10-13 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201013_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
