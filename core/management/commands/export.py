import xlwt
from core.models import Person
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    #def add_arguments(self, parser):
    #    parser.add_argument('file_name', type=str, help='The txt file that contains the journal titles.')

    def handle(self, *args, **kwargs):
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

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
        wb.save('users.xls')

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
