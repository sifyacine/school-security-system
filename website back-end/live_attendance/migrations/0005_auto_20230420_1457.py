# Generated by Django 3.2.5 on 2023-04-20 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registering', '0004_alter_student_full_name'),
        ('live_attendance', '0004_attendance_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registering.student', to_field='full_name'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='id_card',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='number',
            field=models.CharField(default='000', max_length=50),
        ),
        migrations.AddConstraint(
            model_name='attendance',
            constraint=models.UniqueConstraint(fields=('full_name',), name='unique_student_attendance'),
        ),
    ]
