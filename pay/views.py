from asyncio.windows_events import NULL
import calendar
from contextlib import nullcontext
import datetime
from email import message
from sqlite3 import SQLITE_SELECT
from urllib import request
from django.shortcuts import render
import smtplib
from email.message import EmailMessage
from django.core.mail import send_mail
from datetime import datetime
from datetime import date
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Attendance, Employee
from . models import Salary
from . serializers import employeeSerializers
from . serializers import attendanceSerializers
# Added new lib from here
from django.views.generic import View
from .process import html_to_pdf
from django.template.loader import render_to_string
from django.template import loader

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from xhtml2pdf import pisa
from django.core.mail import EmailMultiAlternatives
from rest_framework import viewsets
import sqlite3
from sqlite3 import Error
from .create import check as check

import sqlite3
from datetime import datetime
from datetime import date



global c
# refer following path
# c= r"C:\\Users\\Rohan\\Desktop\\mainproject\\PayRoll_Management_System\\db.sqlite3"
c= r"C:\\Users\\Rohan\\Desktop\\mainproject\\PayRoll_Management_System\\db.sqlite3"



class employeeList(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = employeeSerializers(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = attendanceSerializers

    def create(self, request):
        id = request.POST.get('employee')
        loginTime = request.POST.get('login_Time')
        logoutTime = request.POST.get('logout_Time')
        print("------------------------")
        print(id)
        print(loginTime)
        print(logoutTime)
        print("------------------------")
        res = Attendance.objects.filter(pk = id).update(logout_Time = '2020-9-9 10:15:50')
        print(res)
        print(Attendance.objects.filter(pk = id).update(logout_Time = '2022-8-8 10:15:50'))
        # result = Attendance.objects.raw("SELECT employee_id FROM pay_attendance WHERE id='147' ")
        # self.perform_update(result)
        # # self.serializer_class.save()
        # print(result)
        check(id)

        return HttpResponse("Success")

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = self.getPdf(request)

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
    
    def getPdf(self, request):
        data = Salary.objects.get(pk=request.GET['id'])
        data.salaryMonth = calendar.month_name[int(
            data.workingDay.month)] + ' ' + str(data.workingDay.year)
        data.totalSalaryWithoutTax = data.employee.gross_Salary
        data.totalTax = data.employee.tax + data.employee.provident_Fund
        data.totalNetPay = data.salary
        open('pay/templates/temp.html',
             "w").write(render_to_string('result.html', {'data': data}))

        # Converting the HTML template into a PDF file
        pdf = html_to_pdf('temp.html')

        return pdf

class sendEmail(View):
    def get(self, request):
        data = Salary.objects.get(pk=request.GET['id'])
        data.salaryMonth = calendar.month_name[int(
            data.workingDay.month)] + ' ' + str(data.workingDay.year)

        pdf = GeneratePdf.getPdf(self, request)
        # creates SMTP session
        mail = smtplib.SMTP('smtp.office365.com', 587)
        # start TLS for security
        mail.starttls()
        # content = "PFA Salary Slip OF Bhavesh Khandelwal - "
        msg = EmailMultiAlternatives(
            'Salary Slip of ' + data.salaryMonth,
            'PFA Salary Slip of ' + data.salaryMonth,
            'bhavesh.khandelwal@indiraicem.ac.in',
            [data.employee.email_Address])
        # msg.attach_file(pdf.content)
        msg.attach('invoice.pdf', pdf.content)
        mail.login("bhavesh.khandelwal@indiraicem.ac.in", "Xox25042")

        msg.send()
        print("email send successfully")
        return render(request, "admin/sendEmailSuccess.html")
    # Create your views here.

