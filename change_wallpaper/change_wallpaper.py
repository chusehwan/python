import ctypes
from os import chdir
import os
import shutil
import datetime

#
# def file_size(fname):
#     """파일 크기 측정"""
#     import os
#     statinfo = os.stat(fname)
#     return statinfo.st_size


class lock_screen_file():
    """락스크린 파일별 객체화(크기및 날짜비교등을 위해..)"""

    def __init__(self, file_name, route):
        """Initialize file_name attribute"""
        self.f_name = file_name
        self.route = route

    def file_size(self):
        os.chdir(self.route)
        statinfo = os.stat(self.f_name)
        return statinfo.st_size

#    def file_date(self):




# 경로 : C:\Users\user\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets
# 최초 스폿라이트 파일이 저장되어있는 경로
src_folder =  r'C:\Users\user\Desktop\test_folder'
# 윈도우 스폿라이트 파일이 저장될 D드라이브의 폴더 생성 경로
dest_folder = r'D:\lock_screen'
# D드라이브에 파일이 저장될 폴더를 생성하고 만약 있으면 pass
try:
    os.mkdir(dest_folder)
except FileExistsError:
    pass
# 해당 (소스 폴더) 경로에서 파일 list 가져오기
file_list = os.listdir(src_folder)
# 파일개수 가져오기
num_of_files = len(file_list)
# 파일마다 객체로 만들기
print(file_list[0])
a = lock_screen_file(file_list[0], src_folder)
print(a.file_size())

#
# # 파일 별 수정된 날짜 정보 가져오기
# # 금일자 파일 추리기
# # 해당 파일 복사하여 D드라이브 wall_paper_image폴더에 가져오기
# shutil.copy(file_list[0], dest_folder)
# from_source = dest_folder+'\\'+file_list[0]
# to_source = dest_folder+'\\'+file_list[0]+'.jpg'
# try:
#     os.rename(from_source, to_source)
# except FileExistsError:
#     pass
#
# time = os.path.getmtime(to_source)
# print(time)
# timestamp = datetime.datetime.fromtimestamp(time)
# print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))
# 해당폴더의 파일 list가져오기
# 파일별 수정된 날짜 정보 최신순으로 정렬
# 해당 파일명 확장자 jpg추가

# 배경화면 바꾸기
# ctypes.windll.user32.SystemParametersInfoW(20, 0, r'D:\wall_paper_image\test_screen_3.jpg', 0)