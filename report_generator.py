import openpyxl
from openpyxl import styles
from query_generator import main
from openpyxl.styles import Font, PatternFill, Alignment, alignment
from openpyxl.styles.colors import Color

# main()
wb = openpyxl.load_workbook('F100002645_SQL진단결과보고서.xlsx')
sheet1 = wb.active
print(sheet1)
col = sheet1['F']  # 값이 있는 것만 가져옴


def create_sheet_contents(sheet, file_name, title, sheet_name, column_name):
    # 가운데 정렬, 배경색:#F1F1F1->index:27
    ft = Font(name="휴먼명조", size=9, bold=True)
    color = PatternFill(
        patternType=None, start_color="F1F1F1", end_color="FF1F1F1")
    alignment = Alignment(horizontal="center", vertical="center")
    sheet['A1'] = "진단테이블"
    sheet['A2'] = "진단파일명"
    sheet['A3'] = "진단컬럼"
    sheet['A4'] = "진단항목명"
    sheet['A5'] = "업무규칙 내용"
    sheet['A6'] = "진단 SQL"+"\n"+"(오류 추출 SQL)"

    for a in range(len(sheet['A'])):
        sheet.cell(row=a+1, column=1).font = ft
        sheet.cell(row=a+1, column=1).fill = color
        sheet.cell(row=a+1, column=1).alignment = alignment

    sheet['B1'] = file_name
    sheet['B2'] = title
    sheet['B3'] = sheet_name
    sheet['B4'] = column_name


print('파일 이름을 입력해주세요.')
file_name = input()

# 시트 생성
for c in range(1, len(col)-1):
    if sheet1.cell(row=c, column=6).value == 'Y':
        sheet_name = sheet1.cell(row=c, column=4).value
        sheet = wb.create_sheet(sheet_name)
        title = sheet1.cell(row=c, column=3).value
        column_name = sheet1.cell(row=c, column=5).value
        create_sheet_contents(sheet, file_name, title, sheet_name, column_name)

wb.save('F100002645_SQL진단결과보고서.xlsx')
