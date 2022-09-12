from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import Employee
from . models import Attendance

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_Name','last_Name')
        # fields = '__all__'

class attendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        # fields = ('employee', 'login_Time')
        fields = '__all__'


