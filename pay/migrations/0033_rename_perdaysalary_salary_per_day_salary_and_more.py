# Generated by Django 4.1 on 2022-08-10 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0032_rename_daysinmonth_workingdays_days_in_month_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='perDaySalary',
            new_name='per_Day_Salary',
        ),
        migrations.RenameField(
            model_name='salary',
            old_name='totalSalary',
            new_name='salary',
        ),
        migrations.RenameField(
            model_name='salary',
            old_name='totalSalaryDays',
            new_name='total_Salary_Days',
        ),
    ]
