from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from . models import Employee
from . models import Attendance

class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        # fields = ('firstname','lastname')
        fields = '__all__'
