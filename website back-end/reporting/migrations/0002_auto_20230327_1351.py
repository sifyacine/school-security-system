# Generated by Django 3.2.5 on 2023-03-27 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentreport',
            name='attachment',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='staffreport',
            name='attachment',
            field=models.FileField(upload_to='media'),
        ),
    ]
