import pyperclip
from datetime import datetime
from datetime import date
from os import chdir
import pyautogui
import time
from tkinter import Tk
from datetime import timedelta

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


# date = datetime(year=int(date_num[0:4]), month=int(date_num[4:6]), day=int(date_num[6:8]))
# added_date = date+timedelta(days=add_day)
# converted_date = added_date.strftime("%Y%m%d")

pol_dt = convert_date_1('20200623')
today = str(date.today())
converted_today = convert_date_2(today)



print('pol_dt : ', pol_dt)
print('today :', converted_today)

if pol_dt < converted_today:
    print('pol_dt가 작음')

if pol_dt > converted_today:
    print('pol_dt가 큼')

if pol_dt == converted_today:
    print('같음')

# pol_dt가 금일 날짜보다 작으면 팝업창이 뜸


# if today > com:
#     print('투데이가큼')
# elif today < com:
#     print('com이 큼')