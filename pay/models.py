from calendar import month
from re import S, T
from this import s
from urllib import request
from django.db import models
import calendar
from datetime import datetime
from django.db.models.query_utils import DeferredAttribute
from django.contrib.auth.models import User




# Create your models here.

class Employee(models.Model):
    designation = models.ForeignKey("Designation", related_name="designation_employee", on_delete=models.CASCADE,blank=True,
        null=True)
    first_Name = models.CharField(max_length=10)
    last_Name = models.CharField(max_length=10)
    email_Address = models.EmailField(null=True, unique=True)
    contact_Number = models.PositiveIntegerField(null=True, unique=True)
    pAN_Number = models.CharField(null=True, max_length=25, unique=True)
    bank_Name = models.CharField(null=True, max_length=25)
    account_Number = models.CharField(null=True, max_length=25)
    house_Rent_Allowance = models.IntegerField(null=True)
    allowances = models.IntegerField(null=True)
    conveyance_Allowances = models.IntegerField(null=True)
    tax = models.IntegerField(null=True)
    gross_Salary = models.IntegerField(null=True, blank=True)  
    provident_Fund = models.IntegerField(null=True, blank=True) 
    employee_create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_Name + " " + self.last_Name

    def save(self, *args, **kwargs):
        self.gross_Salary = self.house_Rent_Allowance + self.conveyance_Allowances + self.allowances + self.designation.basic_Salary
        self.provident_Fund = (12*self.designation.basic_Salary) / 100
        print(self.provident_Fund)
        # print(self.gross_Salary)
        return super(Employee, self).save(*args, **kwargs)

class Attendance(models.Model):
    employee = models.ForeignKey("Employee", related_name="attendance_employee", on_delete=models.CASCADE,)
    login_Time = models.DateTimeField()
    logout_Time = models.DateTimeField()
    attendance_create_time = models.DateTimeField(auto_now=True)
    actual_Work_Days = models.CharField(null=True,blank=True,max_length=5)

    def __str__(self):
        return self.employee.first_Name + ' ' + self.employee.last_Name

    def save(self, *args, **kwargs):
        s1 = self.login_Time
        print(s1)
        # s2 = self.logout_Time # for example
        # format = '%H:%M:%S'
        # self.actual_Work_Days  = datetime.strptime(s2, format) - datetime.strptime(s1, format)
        WorkTimeObj = self.logout_Time - self.login_Time
        actualWorkHours = WorkTimeObj.seconds / 3600
        self.actual_Work_Days = 1 if actualWorkHours >= 6 else  0.5
        return super(Attendance, self).save(*args, **kwargs)

class Designation(models.Model):
     title = models.CharField(max_length=15)
     basic_Salary = models.PositiveIntegerField()
    
     def __str__(self):
        return self.title

MONTH_CHOICES = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December'),
)

YEAR_CHOICES = (
    (2022, '2022'),
    (2023, '2023'),
    (2024, '2024'),
    (2025, '2025'),
)

WORKING_CHOICES = (
    (19, '19'),
    (20, '20'),
    (21, '21'),
    (22, '22'),
    (23, '23'),
)

def gen_days(year, month):
    days = calendar.monthrange(year, month)[1]
    return days

def gen_paid_off(work_Days_In_Month, days_In_Month):
    paid = days_In_Month - work_Days_In_Month
    return paid

class WorkingMonth(models.Model, object):
    month = models.IntegerField(choices=MONTH_CHOICES, default=1)
    year = models.IntegerField(choices=YEAR_CHOICES, default=2022)
    work_Days_In_Month = models.IntegerField(choices=WORKING_CHOICES, default=20)
    days_In_Month = models.IntegerField(null=True, blank=True)
    paidOff = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return calendar.month_name[self.month] + ' ' + str(self.year)

    def save(self, *args, **kwargs):
        self.days_In_Month = gen_days(self.year, self.month)
        self.paidOff = gen_paid_off(self.work_Days_In_Month, self.days_In_Month)
        print(self.days_In_Month)
        return super(WorkingMonth, self).save(*args, **kwargs)  

class Salary(models.Model):
    employee = models.ForeignKey("Employee", related_name="salary_employee", on_delete=models.CASCADE,)
    workingDay = models.ForeignKey("WorkingMonth", related_name="salary_workingDay", on_delete=models.CASCADE,)
    total_Salary_Days = models.IntegerField(null=True, blank=True)
    per_Day_Salary = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.employee.first_Name + ' ' + self.employee.last_Name

    def save(self,*args, **kwargs): 
        salaryMonth = str(self.workingDay.year) + '-' + str(self.workingDay.month)
        result= Attendance.objects.raw("select id, strftime('%Y-%m', logout_Time) year_month, sum(actual_Work_Days) actual_Work_Days from pay_attendance where year_month = '2022-07' and employee_id=" + str(self.employee.id) + " group by year_month")[0]
        print(result.year_month)
        # print(result)
        print(result.actual_Work_Days)
        # Show Total Salary Days
        workdayObj = self.workingDay.id
        print(workdayObj)
        r = result.actual_Work_Days
        p = self.workingDay.paidOff
        sum = r + p
        self.total_Salary_Days = sum
        # # Show Salary Per Day 
        grosSalary = self.employee.gross_Salary
        print('----------------------------')
        print(grosSalary)
        print(self.total_Salary_Days)
        dayInMonth = self.workingDay.days_In_Month
        self.per_Day_Salary = grosSalary / dayInMonth
        print(self.per_Day_Salary)
        # # Show Total Salary 
        self.salary = (self.total_Salary_Days * self.per_Day_Salary) - self.employee.tax -self.employee.provident_Fund
        # # print(obj.paidOff)
        # # self.total_Salary_Days = result + obj
        # # print(self.total_Salary_Days)

        return super(Salary, self).save(*args, **kwargs)