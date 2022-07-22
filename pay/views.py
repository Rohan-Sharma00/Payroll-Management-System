from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . models import Attendance
from . serializers import employeeSerializers

class employeeList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = employeeSerializers(employees, many=True)
        return Response(serializer.data)
    def post(self):
        pass


# Create your views here.

