# Generated by Django 4.0.6 on 2022-07-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0019_employee_grosssalary'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary',
            name='perDaySalary',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
