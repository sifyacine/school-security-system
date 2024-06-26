# Generated by Django 3.2.5 on 2023-04-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_attendance', '0005_auto_20230420_1457'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='attendance',
            name='unique_student_attendance',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='id_card',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='photo',
        ),
        migrations.AddField(
            model_name='attendance',
            name='card_id',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendance',
            name='full_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='time_out',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
