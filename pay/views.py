import calendar
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Employee
from . models import Salary
from . serializers import employeeSerializers
# Added new lib from here
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string
from django.template import loader



class employeeList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = employeeSerializers(employees, many=True)
        return Response(serializer.data)
    def post(self):
        pass

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        data = Salary.objects.get(pk=request.GET['id'])
        print('---------------')
        print(data.employee.first_Name)
        data.salaryMonth = calendar.month_name[int(data.workingDay.month)] + ' ' + str(data.workingDay.year)
        data.totalSalaryWithoutTax = data.employee.gross_Salary
        data.totalTax = data.employee.tax + data.employee.provident_Fund
        data.totalNetPay = data.salary
        open('pay/templates/temp.html', "w").write(render_to_string('result.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
# Create your views here.

