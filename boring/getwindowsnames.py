from win32gui import *
import re

titles = set()
titlekey = ''

def foo(hwnd,nouse):
    if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
        titles.add(GetWindowText(hwnd))

EnumWindows(foo, 0)
lt = [t for t in titles if t]
lt.sort()
for t in lt:
    if re.match(titlekey,t):
        print (t)