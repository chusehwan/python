import os

os.chdir(r'D:\2.운영자동화자료\해운스케쥴시스템(Sea Booking Schedule MGT)\KL-Net 검증(edi)')
file_list = os.listdir()

file_object  = open(file_list[2], "r")
contents = file_object.read()
indi_file = contents.split("'")
for i in indi_file:
    print(i)
    print('---------')