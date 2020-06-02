import os
from openpyxl import Workbook
from openpyxl import load_workbook
import pyautogui
from tkinter import Tk
from datetime import datetime
import pyperclip

def value_make(copied_value, column):
    name = column
    divide_values = copied_value.split()

    for i in range(len(divide_values)):
        if divide_values[i] == name:
            return divide_values[i+1]

#copy_v = pyperclip.paste()
#name = value_make(copied_value=copy_v, column = '성명')
#position = value_make(copied_value=copy_v, column = '직위')
#position2 = value_make(copied_value=copy_v, column = '직책')

origin_folder = 'D:\\세환\\python\\사번추출'
image_folder = 'D:\\세환\\python\\사번추출\\image'
file_subject = 'employee_no_result' + '.xlsx'

#print(os.listdir(origin_folder))
#if file_subject in os.listdir(origin_folder):
#    print('파일 있음')


x,y = pyautogui.size()
print(x)
print(y)
x = x/2
y = y/4*3
print(x)
print(y)
pyautogui.click(x,y)










