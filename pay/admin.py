from datetime import datetime
from email.mime import image
from msilib import add_stream
from urllib import request
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.shortcuts import render
from . models import Employee, Salary, WorkingMonth
from . models import Attendance
from django import forms
from django.contrib import messages
from . models import Designation
from . models import Salary
from dateutil.parser import *
from django.utils.html import format_html
import qrcode


class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'login_Time', 'logout_Time',
                    'actual_Work_Days', 'attendance_create_time')

    list_filter = ['employee']

    def get_urls(self):
        urls = super().get_urls()
        upload_urls = [path('upload-csv/', self.upload_csv),]
        scan_urls = [path('scan-qr/', self.scan),]
        return scan_urls + upload_urls + urls

    def upload_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            # Change According to attendance data
            for x in csv_data:
                fields = x.split(",")
                # naveen = parse(str(fields[1]) + ' ' + str(fields[2]))
                # print(naveen)
                # start_date_object = parse(naveen)
                # print(start_date_object)
                # startTime = start_date_object.strftime('%Y%m%d%H%M')
                # end_date_object = self.get_date_object(str(fields[3] + ' ' + fields[4]))
                # endTime = end_date_object.strftime('%Y%m%d%H%M')
                created = Attendance.objects.update_or_create(
                    employee=Employee.objects.get(id=fields[0]),
                    login_Time=parse(str(fields[1]) + ' ' + str(fields[2])),
                    logout_Time=parse(str(fields[3]) + ' ' + str(fields[4])),
                )
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}

        return render(request, "admin/csv_upload.html", data)
    
    def scan(self, request):
        return render(request, "admin/scan_qr.html")


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['title', 'basic_Salary']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_Name', 'last_Name', 'email_Address', 'designation', 'contact_Number', 'pAN_Number', 'bank_Name', 'account_Number',
                    'house_Rent_Allowance', 'allowances', 'conveyance_Allowances', 'tax', 'gross_Salary', 'provident_Fund', 'generate_QR_Code']

    fieldsets = (
        ("Personal Details", {
            "fields": (
                'designation', 'first_Name', 'last_Name', 'email_Address', 'bank_Name', 'account_Number', 'contact_Number', 'pAN_Number'
            ),
        }),
        ("Allowances", {
            "fields": (
                'house_Rent_Allowance', 'allowances', 'conveyance_Allowances', 'tax', 'gross_Salary', 'provident_Fund'
            ),
        }),
    )

    def get_urls(self):
        urls = super().get_urls()
        gen_urls = [path('qr-code/', self.generate),]
        return gen_urls + urls

    def generate(self, request):
        employeeId = request.GET['id']
        fileName = employeeId + ".png"

        # output file name
        filePath = "pay/static/img/qrCodes/" + fileName
        # generate qr code
        img = qrcode.make(employeeId)
        # save img to a file
        img.save(filePath)
        # return HttpResponseRedirect(data)
        imageUrl = 'img/qrCodes/' + fileName
        data = {"imageUrl": imageUrl}
        return render(request, "admin/generate_qr.html", data)

    # Added QR Code For Now

    def generate_QR_Code(self, obj):
        return format_html(f'<a href="/admin/pay/employee/qr-code/?id={obj.id}" style="color:black;">Generate</a>')


class SalaryAdmin(admin.ModelAdmin):
    list_display = ['employee', 'workingDay', 'total_Salary_Days',
                    'per_Day_Salary', 'salary', 'salary_slip']
    list_filter = ['workingDay', 'employee']

    def salary_slip(self, obj):
        return format_html(f'<a href="/pdf/?id={obj.id}" class=default"><b>Print</b></a>')


class workingMonthAdmin(admin.ModelAdmin):
    list_display = ['month', 'year',
                    'work_Days_In_Month', 'days_In_Month', 'paidOff']


# Register your models here.
admin.site.site_header = 'Pay-Roll Management'
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(WorkingMonth, workingMonthAdmin)
admin.site.register(Salary, SalaryAdmin)
