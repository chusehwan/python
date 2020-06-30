import pyperclip
from datetime import datetime
from datetime import date
from os import chdir
import pyautogui
import time
from tkinter import Tk
from datetime import timedelta


def get_subject(title):
    """파일제목 마지막에 저장할 현재일시 및 파일제목 설정"""
    now = datetime.now()
    today = date.today()
    current_time = now.strftime("%H-%M-%S")
    file_name = title + str(today) + '_' + str(current_time) + '.xlsx'
    return file_name


def get_value_make_excel(ws):
    """클립보드에 복사된 컨넘버, pol dt, pod dt 값을 분리하여 워크시트에 저장"""
    ws.cell(1, 1).value = 'So_No'
    ws.cell(1, 2).value = 'CNTR_No'
    ws.cell(1, 3).value = 'POL_DT'
    ws.cell(1, 4).value = 'POD_DT'
    init_row_num = 2
    init_column_num = 2
    copy_v = pyperclip.paste()
    div_v = copy_v.split()
    num_of_cntr = int(len(div_v) / 3)
    for i in range(len(div_v)):
        ws.cell(init_row_num, init_column_num).value = div_v[i]
        init_column_num += 1
        if init_column_num > 4:
            init_column_num = 2
            init_row_num += 1
    return ws, num_of_cntr


def get_value_make_excel_2(ws):
    """클립보드에 복사된 컨넘버, pol dt, pod dt 값을 분리하여 워크시트에 저장"""
    ws.cell(1, 1).value = 'CNTR_No'
    ws.cell(1, 2).value = 'Result'
    init_row_num = 2
    init_column_num = 1
    copy_v = pyperclip.paste()
    div_v = copy_v.split()
    num_of_cntr = int(len(div_v))
    for i in range(len(div_v)):
        ws.cell(init_row_num, init_column_num).value = div_v[i]
        init_row_num += 1
    return ws, num_of_cntr


def get_value_make_excel_for_dp(ws):
    """클립보드에 복사된 컨넘버, pol dt, pod dt 값을 분리하여 워크시트에 저장, 컨넘버 앞 4자리가 PKEU이면 PASS함"""
    ws.cell(1, 1).value = 'CNTR_No'
    ws.cell(1, 2).value = 'Result'
    init_row_num = 2
    init_column_num = 1
    copy_v = pyperclip.paste()
    div_v = copy_v.split()
    # 앞자리가 PKEU인건은 LIST에서 제거
    not_pkeu_list = []
    for i in div_v:
        if i[:4] != 'PKEU':
            not_pkeu_list.append(i)
    num_of_cntr = int(len(not_pkeu_list))
    for i in range(len(not_pkeu_list)):
        ws.cell(init_row_num, init_column_num).value = not_pkeu_list[i]
        init_row_num += 1
    return ws, num_of_cntr, not_pkeu_list

def get_value_make_excel_for_so(ws):
    """클립보드에 복사된 so넘버 값을 워크시트에 저장"""
    ws.cell(1, 1).value = 'SO_No'
    ws.cell(1, 2).value = 'DBL_No'
    # ws.cell(1, 3).value = 'Result'
    init_row_num = 2
    init_column_num = 1
    copy_v = pyperclip.paste()
    div_v = copy_v.split()
    # 앞자리가 PKEU인건은 LIST에서 제거
    so_list = []
    for i in div_v:
        so_list.append(i)
    num_of_so = int(len(so_list))
    for i in range(len(so_list)):
        ws.cell(init_row_num, init_column_num).value = so_list[i]
        init_row_num += 1
    return ws, num_of_so, so_list


def image_search_click(file_name, image_folder, x=0, y=0, confidence_parameter = 0.8):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지 명과 이미지폴더, x,y값을 바탕으로 화면상 해당이미지 검색 및 클릭(찾을때까지)"""
    chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name, confidence = confidence_parameter)
        if location is None:
            print(file_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            continue
        else:
            x_co, y_co = pyautogui.locateCenterOnScreen(file_name, confidence = confidence_parameter)
            x_co += x
            y_co += y
            pyautogui.click(x_co, y_co)
            pyautogui.PAUSE = 0.3
            break


def image_search_double_click(file_name, image_folder, x=0, y=0, confidence_parameter = 0.8):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지 명과 이미지폴더, x,y값을 바탕으로 화면상 해당이미지 검색 및 클릭(찾을때까지)"""
    chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name, confidence=confidence_parameter)
        if location is None:
            print(file_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            continue
        else:
            x_co, y_co = pyautogui.locateCenterOnScreen(file_name, confidence=confidence_parameter)
            x_co += x
            y_co += y
            pyautogui.doubleClick(x_co, y_co)
            pyautogui.PAUSE = 0.1
            break


def both_image_search_double_click(file_name_1, file_name_2, image_folder, x=0, y=0, confidence_parameter = 0.8):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지 명과 이미지폴더, x,y값을 바탕으로 첫번째 이미지와 두번째 이미지를
    화면상 찾을 때 까지 검색하고 하나라도 찾으면 찾은이미지를 클릭"""
    chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name_1, confidence = confidence_parameter)
        location2 = pyautogui.locateCenterOnScreen(file_name_2, confidence = confidence_parameter)
        if location is None and location2 is None:
            print(file_name_1 + ',' + file_name_2 + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            continue
        elif location is not None:
            x_co, y_co = pyautogui.locateCenterOnScreen(file_name_1, confidence = confidence_parameter)
            x_co += x
            y_co += y
            pyautogui.doubleClick(x_co, y_co)
            pyautogui.PAUSE = 0.1
            break
        else:
            x_co, y_co = pyautogui.locateCenterOnScreen(file_name_2, confidence = confidence_parameter)
            x_co += x
            y_co += y
            pyautogui.doubleClick(x_co, y_co)
            pyautogui.PAUSE = 0.1
            break


def image_search_only(file_name, image_folder, confidence_parameter = 0.8):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지를 찾을때까지 대기함, 찾으면 break"""
    chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name, confidence = confidence_parameter)
        if location is None:
            print(file_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            continue
        else:
            pyautogui.PAUSE = 0.1
            break


def image_search_only_once(file_name, image_folder, confidence_parameter = 0.8):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지를 찾을때까지 대기함, 찾으면 break"""
    chdir(image_folder)
    location = pyautogui.locateCenterOnScreen(file_name, confidence = confidence_parameter)
    if location is None:
        print(file_name + '이미지 찾지 못함')
        pyautogui.PAUSE = 0.3
        return 'No_image'
    else:
        pyautogui.PAUSE = 0.1
        return 'find_image'


def image_check_n_click(file_name, file_name2, image_folder, confidence_parameter = 0.8):
    """첫이미지를 화면상 검색시도하고 찾지못하면 두번째이미지를 화면상 검색하여 클릭 함
    첫이미지를 찾게되면 break"""
    chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name, confidence = confidence_parameter)
        if location is None:
            print(file_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            image_search_click(file_name2, image_folder)
            pyautogui.PAUSE = 0.3
            continue
        else:
            pyautogui.PAUSE = 0.1
            break


def sleep(num):
    time.sleep(num)


def data_clear_input(data):
    """전체선택 후 지운 후 전달받은 data값을 입력함"""
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.3)
    pyautogui.press('backspace')
    pyautogui.write(data)


def check_PKEU(cntr_no, image_folder):
    """컨테이너 앞글자가 PKEU 로 시작하면 쉽먼트타입을 맷치백으로 바꾸고 아니면 그냥 원본대로 진행"""
    init_4 = cntr_no[:4]
    if init_4 == 'PKEU':
        image_search_double_click(file_name='Shipment_Type.png', image_folder=image_folder, x=0, y=0)
        time.sleep(0.1)
        pyautogui.press('down')
        time.sleep(0.1)
        pyautogui.press('pagedown')
        time.sleep(0.1)
        for i in range(5):
            pyautogui.press('up')
            time.sleep(0.1)
        pyautogui.press('tab')


def input_dt(dt, image_name, image_folder):
    """전달된 이미지를 더블클릭하여 탭 한 후 데이터삭제 및 dt값 입력"""
    time.sleep(0.1)
    image_search_double_click(image_name, image_folder)
    for i in range(5):
        time.sleep(0.1)
        pyautogui.press('tab')
    time.sleep(0.1)
    data_clear_input(dt)


def check_err_click_close(check_image_name, click_image_name, image_folder):
    """past date 입력해서 에러메시지 뜰 경우 해당 팝업창 닫아주기"""
    time.sleep(1)
    chdir(image_folder)
    for i in range(5):
        location = pyautogui.locateCenterOnScreen(check_image_name)
        if location is None:
            print(check_image_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.3
            continue
        else:
            pyautogui.PAUSE = 0.1
            image_search_click(click_image_name, image_folder)
            break


def check_column_value(image_name, image_folder, x=0, y=0):
    """전달받은 값을 바탕으로 해당 이미지 하단 더블클릭 후 값을 복사하여 반환"""
    image_search_double_click(image_name, image_folder,x, y)
    sleep(0.1)
    pyperclip.copy('')
    pyautogui.hotkey('ctrl','c')
    try:
        copied_value = Tk().clipboard_get()
    except:
        copied_value = ''
    return copied_value


def convert_date(date_num, add_day= 0):
    """8자리 숫자를 하루  date값으로 변환"""
    # you could also import date instead of datetime and use that.
    date = datetime(year=int(date_num[0:4]), month=int(date_num[4:6]), day=int(date_num[6:8]))
    added_date = date+timedelta(days=add_day)
    converted_date = added_date.strftime("%Y%m%d")

    return converted_date


def convert_date_1(date_num, add_day= 0):
    """8자리 숫자를 하루  date 값으로 변환"""
    # you could also import date instead of datetime and use that.
    date = datetime(year=int(date_num[0:4]), month=int(date_num[4:6]), day=int(date_num[6:8]))
    return date


def convert_date_2(date_num, add_day= 0):
    """10자리 숫자를 하루  date 값으로 변환 예)2020-06-23"""
    # you could also import date instead of datetime and use that.
    date = datetime(year=int(date_num[0:4]), month=int(date_num[5:7]), day=int(date_num[8:10]))
    return date


def check_date_err_click_close(image_name, port_date, image_folder):
    """입력받은 date를 바탕으로 금일기준 과거인지 여부 판단하여 과거일 시 전달받은 image를 클릭함"""
    port_date = convert_date_1(port_date)
    today = str(date.today())
    converted_today = convert_date_2(today)
    if port_date < converted_today:
        image_search_double_click(image_name, image_folder)


def check_date_err_click_close_last(image_name, port_date_1, port_date_2, image_folder):
    """입력받은 podl, pod date를 바탕으로 금일기준 과거인지 여부 판단하여 과거일 시 전달받은 image를 클릭함"""
    port_date_1 = convert_date_1(port_date_1)
    port_date_2 = convert_date_1(port_date_2)
    today = str(date.today())
    converted_today = convert_date_2(today)
    if port_date_1 < converted_today or port_date_2 < converted_today:
        image_search_click(image_name, image_folder)


def last_check(image_name_1, image_name_2, image_folder):
    err = ''
    suc = ''
    while True:
        err = image_search_only_once(image_name_1, image_folder)
        suc = image_search_only_once(image_name_2, image_folder)
        if err == 'find_image' or suc == 'find_image':
            break
    if err == 'find_image':
        image_search_click(image_name_1, image_folder)
        return 'err'
    if suc == 'find_image':
        image_search_click(image_name_2, image_folder)
        return 'suc'



