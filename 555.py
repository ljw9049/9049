import xlsxwriter
from datetime import datetime

now = datetime.now().date()
nowstring = datetime.strftime(now,'%Y%m%d')
filename = 'result.csv'

file = open("/var/lib/awx/projects/_11__ljw90/Result/result.csv", 'r')
data = file.readlines()
workbook = xlsxwriter.Workbook('/var/lib/awx/projects/_11__ljw90/result.xlsx')
worksheet = workbook.add_worksheet('Sheet')
format = workbook.add_format({'bold': True, 'align': 'center'})
format.set_border()
format.set_pattern(1)
format.set_bg_color('#A9BCF5')

row = 1
col = 0
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)
worksheet.write(0, 0, 'Hostname', format)
worksheet.write(0, 1, 'NAME', format)
worksheet.write(0, 2, 'DESCR', format)
worksheet.write(0, 3, 'PID', format)
worksheet.write(0, 4, 'VID', format)
worksheet.write(0, 5, 'SN', format)

for i in data:
    for j in i.split(','):
        worksheet.write(row, col, j)
        col += 1
    col = 0
    row += 1


workbook.close()
