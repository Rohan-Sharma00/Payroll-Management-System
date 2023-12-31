# Generated by Django 4.1 on 2022-08-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0034_rename_workingdays_workingday'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='contact_Number',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='pAN_Number',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='account_Number',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
    ]
