# Generated by Django 3.2.5 on 2023-04-20 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registering', '0002_auto_20230324_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='encodings_file',
            field=models.CharField(default=1233, max_length=255),
            preserve_default=False,
        ),
    ]