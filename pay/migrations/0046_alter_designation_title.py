# Generated by Django 4.1 on 2022-09-06 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0045_alter_employee_account_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]