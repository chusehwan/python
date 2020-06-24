import os
from openpyxl import Workbook
import pyautogui
from tkinter import Tk
from datetime import datetime

def copy_right_value(file_name, tab_num, route):
    os.chdir(route)
    location = pyautogui.locateCenterOnScreen(file_name)
    pyautogui.doubleClick(location)
    # 탭
    for i in range(tab_num):
        pyautogui.press('tab')
    pyautogui.PAUSE = 0.1
    # 사번 클립보드에 복사
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.PAUSE = 0.1
    copied_value = Tk().clipboard_get()
    return copied_value

def save_value_in_excel(ws, current_copied_employee_id, a, column_num, route):
    os.chdir(route)
    # 대상 셀 객체화
    pyautogui.PAUSE = 0.1
    target_cell = ws.cell(a+1,column_num)
    target_cell.value = current_copied_employee_id

def image_search_click(file_name, route):
    # ※주의※ 파일명 영어만 됨
    os.chdir(route)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name)
        if location == None:
            print('이미지 찾지 못함')
            continue
        else:
            pyautogui.doubleClick(location)
            pyautogui.PAUSE = 0.1
            break

def check_down(a, max_row_num):
    mod = a % max_row_num
    if mod != 0:
        pyautogui.press('down')

def file_save(origin_folder, file_subject):
    os.chdir(origin_folder)
    wb.save(file_subject)

# 메인 코드
origin_folder = 'D:\\세환\\python\\사번추출'
image_folder = 'D:\\세환\\python\\사번추출\\image'
wb = Workbook()
ws = wb.active
current_copied_employee_id = 'initialize'
previous_copy_id = None

total_no = 30
max_row_num = 4

for a in range(total_no):   
    mod2 = a % max_row_num
    if a>0 and mod2 == 0 :
        image_search_click(file_name='page_change.png', route = image_folder)
        pyautogui.PAUSE = 1
        pyautogui.press('pageup')
    # 활성화 줄 클릭
    image_search_click('active_list_value.png', route = image_folder)
    # 내리기 여부 결정
    check_down(a = a, max_row_num = max_row_num)
    # 메인 데이터 부분(사번) 클릭 및 변수에 사번 저장, 사번이 제대로 저장되었나 확인후 안되면 다시 클릭
    while True:
        current_copied_employee_id = copy_right_value('employee_id.png', tab_num = 1, route = image_folder)
        test_cpy = len(current_copied_employee_id)
        if current_copied_employee_id != previous_copy_id or test_cpy == 5:
            break
        image_search_click('active_list_value.png', route = image_folder)

    previous_copy_id = current_copied_employee_id
    # 저장된 사번 변수 엑셀파일에 저장
    save_value_in_excel(ws, current_copied_employee_id, a, column_num = 1, route = origin_folder)
    current_copied_employee_id = 'initialize'
    # 메인 데이터 부분(사번) 클릭 및 변수에 사번 저장
    current_copied_status = copy_right_value('status.png', tab_num = 2, route = image_folder)
    # 저장된 status 변수 엑셀파일에 저장
    save_value_in_excel(ws, current_copied_status, a, column_num = 2, route = origin_folder)
    if current_copied_status == '퇴직':
        # 메인 데이터 부분(퇴직일) 클릭 및 변수에 사번 저장
        current_copied_retired_dt = copy_right_value('retire_date.png', tab_num=1, route=image_folder)
        # 저장된 퇴직일 변수 엑셀파일에 저장
        save_value_in_excel(ws, current_copied_retired_dt, a, column_num=3, route=origin_folder)
    pyautogui.PAUSE = 0.1
    # 파일 저장기능
    file_subject = 'employee_no_result' + '.xlsx'
    file_save(origin_folder=origin_folder, file_subject = file_subject)

