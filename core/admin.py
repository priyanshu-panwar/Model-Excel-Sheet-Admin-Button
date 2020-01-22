from django.contrib import admin
from .models import Person
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import PersonForm
import xlwt
from django.urls import path

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
	change_list_template = 'core/Person_changelist.html'

	def get_urls(self):
		urls = super().get_urls()
		my_urls = [
			path('export/', self.export_users),
		]
		return my_urls + urls


	def export_users(self, request):
	    response = HttpResponse(content_type='application/ms-excel')
	    response['Content-Disposition'] = 'attachment; filename="users.xls"'

	    wb = xlwt.Workbook(encoding='utf-8')
	    ws = wb.add_sheet('Person')

	    # Sheet header, first row
	    row_num = 0

	    font_style = xlwt.XFStyle()
	    font_style.font.bold = True

	    columns = ['Username', 'First name', 'Last name', 'Email address', ]

	    for col_num in range(len(columns)):
	        ws.write(row_num, col_num, columns[col_num], font_style)

	    # Sheet body, remaining rows
	    font_style = xlwt.XFStyle()

	    rows = Person.objects.all().values_list('firstname', 'lastname', 'email')
	    for row in rows:
	        row_num += 1
	        for col_num in range(len(row)):
	            ws.write(row_num, col_num, row[col_num], font_style)

	    wb.save(response)
	    return response