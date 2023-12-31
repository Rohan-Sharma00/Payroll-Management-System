# Generated by Django 4.1 on 2022-08-20 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0043_rename_workingday_workingmonth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingmonth',
            name='month',
            field=models.CharField(choices=[('01', 'January'), ('02', 'February'), ('03', 'March'), ('04', 'April'), ('05', 'May'), ('06', 'June'), ('07', 'July'), ('08', 'August'), ('09', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default='01', max_length=2),
        ),
        migrations.AlterField(
            model_name='workingmonth',
            name='year',
            field=models.CharField(choices=[('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2022', max_length=4),
        ),
    ]
