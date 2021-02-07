import openpyxl
import xlrd
import xlwt
import os
a=os.getcwd()  #获取当前路径
print(a)
workbook_1=openpyxl.load_workbook("寒假分期计划表.xlsx")  #读取Pycharm工作簿,返回一个workbook对象
b=workbook_1.sheetnames
print(b)  #调用函数,获取工作簿中工作表名称
# sheet1=workbook_1.get_sheet_by_name('快捷键的使用')  #返回一个worksheet对象
# print(sheet1.title)  #利用属性title打印worksheet对象的名称
# """s=workbook_1.get_active_sheet()
# print(s)"""
# print(sheet1.get_highest_row())

