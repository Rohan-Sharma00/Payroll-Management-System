# Generated by Django 4.1 on 2022-08-10 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0033_rename_perdaysalary_salary_per_day_salary_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkingDays',
            new_name='WorkingDay',
        ),
    ]
