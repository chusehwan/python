import os
import pyautogui
import switch_app as sa
import time

def image_search_click(file_name, image_folder, x=0, y=0):
    # ※주의※ 파일명 영어만 됨
    """전달된 이미지 명과 이미지폴더, x,y값을 바탕으로 화면상 해당이미지 검색 및 클릭(찾을때까지)"""
    os.chdir(image_folder)
    while True:
        location = pyautogui.locateCenterOnScreen(file_name, grayscale=True)
        if location is None:
            print(file_name + '이미지 찾지 못함')
            pyautogui.PAUSE = 0.1
            continue
        else:
            x_co, y_co = pyautogui.locateCenterOnScreen(file_name,grayscale=True)
            x_co += x
            y_co += y
            pyautogui.click(x_co, y_co)
            pyautogui.PAUSE = 0.1
            break

# sa.switch_app()
os.chdir(r'D:\세환\python\container_part\image_so_creation')
image_folder = r'D:\세환\python\container_part\image_so_creation'
for i in range(10):
    x_co, y_co = pyautogui.locateCenterOnScreen('test_1.png', grayscale=True)
    print(x_co)
    print(y_co)
    x_co, y_co = pyautogui.locateCenterOnScreen('test_2.png', grayscale=True)
    print(i)



print('프로그램 끝 ^0^')
print('총소요시간(초) : ', round(time.perf_counter(), 2))
print('건당소요시간(초) : ', round((time.perf_counter()/i), 2))