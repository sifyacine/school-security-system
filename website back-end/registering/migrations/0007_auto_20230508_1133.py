# Generated by Django 3.2.5 on 2023-05-08 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registering', '0006_auto_20230507_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='student',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]