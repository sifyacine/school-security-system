# Generated by Django 3.2.5 on 2023-05-09 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_attendance', '0006_auto_20230420_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
