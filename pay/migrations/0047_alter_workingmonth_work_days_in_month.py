# Generated by Django 4.1 on 2022-09-06 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0046_alter_designation_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingmonth',
            name='work_Days_In_Month',
            field=models.IntegerField(choices=[(18, '18'), (19, '19'), (20, '20'), (21, '21'), (22, '22'), (23, '23')], default=20),
        ),
    ]
