# Generated by Django 4.0.6 on 2022-07-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0008_attendance_actualworkingdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='actualWorkingDays',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
