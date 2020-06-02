import os
from openpyxl import Workbook
import pyperclip


def value_make(copied_value):
    '''클립보드에서 가져온 값 나눠주기(앞3자리 뺀값으로 list에 저장)'''
    divide_values = copied_value.split('미리보기')
    return divide_values


origin_folder = 'D:\\'
os.chdir(origin_folder)
wb = Workbook()
ws = wb.active
row_num = 1
copy_v = pyperclip.paste()
divided_values = value_make(copied_value=copy_v)
for i in divided_values:
    if '재무회계팀' in i:
        print(i)



