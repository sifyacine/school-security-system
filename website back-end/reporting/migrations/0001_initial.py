# Generated by Django 3.2.5 on 2023-03-24 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registering', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=255)),
                ('report_content', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registering.student')),
            ],
        ),
        migrations.CreateModel(
            name='StaffReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
                ('attachment', models.FileField(upload_to='attachments/')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registering.staff')),
            ],
        ),
    ]
