from django.db import models

# Create your models here.

class Employee(models.Model):
    designation = models.ForeignKey("Designation", related_name="designation_employee", on_delete=models.CASCADE,blank=True,
        null=True)
    firstname = models.CharField(max_length=10)
    lasstname = models.CharField(max_length=10)
    employee_create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstname + " " + self.lasstname
    
class Attendance(models.Model):
    employee = models.ForeignKey("Employee", related_name="attendance_employee", on_delete=models.CASCADE,)
    date = models.CharField(max_length=10)
    loginTime = models.CharField(max_length=10)
    logoutTime = models.CharField(max_length=10)
    attendance_create_time = models.DateTimeField(auto_now=True)


    def __int__(self):
        return self.date

class Designation(models.Model):
     title = models.CharField(max_length=15)
     baseSalary = models.PositiveIntegerField()
    
     def __str__(self):
        return self.title