import xlsxwriter

file = open("/var/lib/awx/projects/_11__ljw90/Result/cisco.log", 'r')
data = file.readlines()
workbook = xlsxwriter.Workbook('/var/lib/awx/projects/_11__ljw90/cisco.xlsx')
worksheet = workbook.add_worksheet('Result')
format = workbook.add_format({'bold': True, 'align': 'center'})
format.set_border()
format.set_pattern(1)
format.set_bg_color('#A9BCF5')

format2 = workbook.add_format()
format2.set_border()
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 15)
worksheet.set_column('C:C', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('E:E', 15)
worksheet.set_column('F:F', 15)
worksheet.set_column('G:G', 15)
worksheet.set_column('H:H', 15)
worksheet.set_column('I:I', 15)
worksheet.set_column('J:J', 15)
worksheet.set_column('K:K', 15)
worksheet.set_column('L:L', 15)
worksheet.set_column('M:M', 15)

worksheet.write(0, 0, 'Name', format)
worksheet.write(1, 1, 'SN', format)
worksheet.write(2, 2, 'Pid', format)


row = 1
col = 0

for i in data:
    for j in i.split('___'):
        worksheet.write(row, col, j, format2)
        col += 1
    col = 0
    row += 1

workbook.close()



