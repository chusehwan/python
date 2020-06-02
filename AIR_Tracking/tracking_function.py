import os
from openpyxl import Workbook
import pyperclip
from datetime import datetime
from datetime import date


def get_subject():
    '''파일제목 마지막에 저장할 현재일시 및 파일제목 설정'''
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H-%M-%S")
    file_name = 'Tracking_result_'+str(today)+'_'+str(current_time)+'.xlsx'
    return file_name


def value_make(copied_value):
    '''클립보드에서 가져온 값 나눠주기(앞3자리 뺀값으로 list에 저장)'''
    divide_values = copied_value.split()
    return divide_values


def verifi_awb(awb_list):
    '''awb넘버 바탕 앞 3자리 기준으로 대한항공,아시아나 정리'''
    ke_list=[]
    oz_list=[]
    for i in awb_list:
        if i[:3] == '180':
            ke_list.append(i)
        elif i[:3] == '988':
            oz_list.append(i)
    total_list = ke_list+oz_list
    return total_list, ke_list, oz_list


def file_save(origin_folder, file_subject, wb):
    '''파일 지정 폴더에 저장'''
    os.chdir(origin_folder)
    wb.save(file_subject)