# Generated by Django 4.0.6 on 2022-07-30 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0012_alter_attendance_actualworkdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='allowances',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='conveyanceAllowances',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='houseRentAllowance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='tax',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalSalaryDay', models.IntegerField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_employee', to='pay.employee')),
                ('workingDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_workingDay', to='pay.workingdays')),
            ],
        ),
    ]
