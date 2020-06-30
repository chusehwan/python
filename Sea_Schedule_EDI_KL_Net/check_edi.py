import os

os.chdir(r'D:\2.운영자동화자료\해운스케쥴시스템(Sea Booking Schedule MGT)\KL-Net 검증(edi)')
file_list = os.listdir()
def get_vessel_name(a):
    for y in range(len(a)):
        check_matter = a[y]+a[y+1]
        if check_matter == '::':
            vessel_name = a[y+2:]
            return vessel_name


for i in range(len(file_list)):
    file_object  = open(file_list[i], "r")
    contents = file_object.read()
    indi_file = contents.split("'")
    print('file name : ', file_list[i])
    for a in indi_file:
        if 'LOC+88' in a:
            print('출발항 : ', a[7:12])
        if 'LOC+7' in a:
            print('도착항 : ', a[6:11])
        if 'DTM+137' in a:
            print('EDI문서 전송일시 : ', a[8:18])
        if 'DTM+222' in a:
            print('Docu Closing : ', a[8:18])
        if 'DTM+180' in a:
            print('Cargo Closing : ', a[8:18])
        if 'DTM+133' in a:
            print('ETD : ', a[8:18])
        if 'DTM+132' in a:
            print('ETA : ', a[8:18])
        if 'DTM+189' in a:
            print('Scheduled.T.D : ', a[8:18])
        if 'TDT+20' in a:
            vsl_name = get_vessel_name(a)
            print('Vessel Name : ', vsl_name)
    print('--------------------------------------')
    file_object.close()
