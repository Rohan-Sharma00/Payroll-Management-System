# Generated by Django 4.1 on 2022-08-10 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0027_rename_lasstname_employee_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='firstname',
            new_name='first_Name',
        ),
    ]