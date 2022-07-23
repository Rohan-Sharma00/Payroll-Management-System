from datetime import date
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path, reverse
from django.shortcuts import render
from . models import Employee
from . models import Attendance
from django import forms
from django.contrib import messages
from . models import Designation


class CsvImportForm(forms.Form):
	csv_upload = forms.FileField()	

class AttendanceAdmin(admin.ModelAdmin):
	def get_urls(self):
		urls = super().get_urls()
		new_urls = [path('upload-csv/', self.upload_csv), ]
		return new_urls + urls

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
				created = Attendance.objects.update_or_create(
                    date = fields[0],
                    loginTime = fields[1],
					logoutTime = fields[2],
					employee = Employee.objects.get(id = fields[3])
                    )
			url = reverse('admin:index')
			return HttpResponseRedirect(url)

		form = CsvImportForm()
		data = {"form": form}

		return render(request, "admin/csv_upload.html", data)

# Register your models here.
admin.site.site_header = 'Pay-Roll Management'
admin.site.register(Employee)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Designation)

 

