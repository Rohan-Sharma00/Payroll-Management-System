# Generated by Django 4.0.6 on 2022-07-27 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0004_remove_designation_employee_employee_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=10)),
                ('year', models.CharField(max_length=10)),
                ('totalWorking', models.CharField(choices=[('19', 'Nineteen'), ('20', 'Twenty'), ('21', 'Twenty-one'), ('22', 'Twenty-two')], default='20', max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='loginTime',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='logoutTime',
            field=models.TimeField(null=True),
        ),
    ]
