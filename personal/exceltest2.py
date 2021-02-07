import openpyxl
wb=openpyxl.load_workbook('寒假分期计划表.xlsx')
wb1=openpyxl.load_workbook("PyCharm.xlsx")
print(wb1.worksheets)
print(wb.sheetnames)
print(wb.read_only)
print(wb1.properties)