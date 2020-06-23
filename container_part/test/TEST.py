from openpyxl import Workbook
from tkinter import Tk
import functions as fn
import switch_app as sa
import pyautogui
import time
from os import chdir

image_folder = r'D:\세환\python\container_part\image_so_creation'
save_folder = 'D:\\'

# 익스플로러 창 열기
sa.switch_app()

fn.image_search_double_click('Save.png', image_folder)
fn.sleep(0.2)
fn.image_search_double_click('test_1.png', image_folder)
fn.sleep(0.2)
fn.image_search_double_click('confirm.png', image_folder)
print('끝')