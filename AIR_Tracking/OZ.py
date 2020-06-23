from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def convert_oz_time_info(value,info):
    '''대한항공 트래킹 웹사이트에서 복사된 일자값을 통일된 양식(2020-05-20 18:00)으로 가공'''
    if info == 'atd':
        result = value[17:]
    elif info == 'ata':
        result = value[15:]
    # 크롤링된 값 공통 값으로 정리하기(ex) departure date 2020 18:00 -> 2020-03-24 18:00)
    return result


def check_screen_result(driver, row_num, awb_num, ws):
    while True:
        try:
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="R'+awb_num+'"]/div/div/div[1]/div[1]/h4')
            break
        except:
            pass
            try:
                time.sleep(0.3)
                driver.find_element_by_xpath('//*[@id="noResultSection"]/div/div')
                # 만약 검색결과가 없을 시 추가 절차 생략 및 remark란에 no_data기입 후 다음 AWB조회
                ws.cell(row_num, 6).value = 'No_data'
                driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div/input[2]').clear()
                row_num += 1
                return 'no'
                break
            except:
                pass

def check_pcs(driver, awb_num, status):
    """shpiment history상 명시된 PCS 수량을 찾아서 반환"""
    ini_num = 1
    try:
        while True:
            # //*[@id="historyInfo_98825818262"]/tbody/tr[6]/td[1] <- BKD 문자 주소
            BKD_Address = '//*[@id="historyInfo_' + awb_num + '"]/tbody/tr['+str(ini_num)+']/td[1]'
            if driver.find_element_by_xpath(BKD_Address).text != status:
                ini_num += 1
            if driver.find_element_by_xpath(BKD_Address).text == status:
                break
        PCS_address = '//*[@id="historyInfo_' + awb_num + '"]/tbody/tr['+str(ini_num)+']/td[5]'
        check_pcs =  driver.find_element_by_xpath(PCS_address)
        return check_pcs.text
    except:
        return None


def get_flight_info(driver, awb_num, dept_pcs, arr_pcs):
    """STD, ATD, STA, ATA정보 추출"""
    info_address_departure = '//*[@id="bookingInfo_'+awb_num+'"]/tbody/tr/td[4]'
    info_address_arrival = '//*[@id="bookingInfo_' + awb_num + '"]/tbody/tr/td[5]'
    departure_info = driver.find_element_by_xpath(info_address_departure).text
    arrival_info = driver.find_element_by_xpath(info_address_arrival).text
    splited_d_info = departure_info.split('\n')
    splited_a_info = arrival_info.split('\n')

    info_address_departure_2 = '//*[@id="bookingInfo_' + awb_num + '"]/tbody/tr[2]/td[4]'
    info_address_arrival_2 = '//*[@id="bookingInfo_' + awb_num + '"]/tbody/tr[2]/td[5]'
    try:
        departure_info_2 = driver.find_element_by_xpath(info_address_departure).text
        splited_d_info_2 = departure_info.split('\n')
    except:
        pass
    try:
        arrival_info_2 = driver.find_element_by_xpath(info_address_arrival).text
        splited_a_info_2 = arrival_info.split('\n')
    except:
        pass
    STD = splited_d_info[0][:16]
    STA = splited_a_info[0][:16]
    ATD = ''
    ATA = ''
    """ ATD 관련 정리 """
    # CASE1. Departure관련 첫줄에 STD 만 나오고 둘쨋줄이 있고, 출발을 한 경우
    if len(splited_d_info) == 1 and dept_pcs != None and len(splited_d_info_2) == 2:
        ATD = splited_d_info_2[1][:16]
    # CASE2. Departure관련 첫줄에 STD, ATD 나온 경우
    elif len(splited_d_info) == 2:
        ATD = splited_d_info[1][:16]
    # CASE3. Departure관련 첫줄에 STD, ETD, ATD 나온 경우
    elif len(splited_d_info) == 3:
        ATD = splited_d_info[2][:16]
    # CASE4. Departure관련 첫줄엔 STD만 둘쨋줄에 STD, ATD 나온 경우
    elif len(splited_d_info) == 1 and len(splited_d_info_2) == 2:
        ATD = splited_d_info_2[1][:16]
    # CASE5. Departure관련 첫줄엔 STD만 둘쨋줄엔 STD, ETD, ATD 나온 경우
    elif len(splited_d_info) == 1 and len(splited_d_info_2) == 3:
        ATD = splited_d_info_2[2][:16]

    """ ATA 관련 정리 """
    # CASE1. Arrival관련 첫줄에 STA 만 나오고 둘쨋줄이 있고, 도착을 한 경우
    if len(splited_a_info) == 1 and arr_pcs != None and len(splited_a_info_2) == 2:
        ATA = splited_a_info_2[1][:16]
    # CASE2. Arrival관련 첫줄에 STA, ATA 나온 경우
    elif len(splited_a_info) == 2 :
        ATA = splited_a_info[1][:16]
    # CASE3. Arrival관련 첫줄에 STA, ETA, ATA 나온 경우
    elif len(splited_a_info) == 3:
        ATA = splited_a_info[2][:16]
    # CASE4. Arrival관련 첫줄엔 STA만 둘쨋줄에 STA, ATA 나온 경우
    elif len(splited_a_info) == 1 and len(splited_a_info_2) == 2:
        ATA = splited_a_info_2[1][:16]
    # CASE5. Arrival관련 첫줄엔 STA만 둘쨋줄엔 STA, ETA, ATA 나온 경우
    elif len(splited_a_info) == 1 and len(splited_a_info_2) == 3:
        ATD = splited_a_info_2[2][:16]
    flight_info_list=[]
    flight_info_list.append(STD)
    flight_info_list.append(ATD)
    flight_info_list.append(STA)
    flight_info_list.append(ATA)
    return flight_info_list


def get_tracking_info_oz(list, driver_dir, original_row_num, ws):
    """아시아나 홈페이지 접속 및 트랙킹 작업 awb list 바탕 진행"""
    oz_len = len(list)
    chromedriver_dir = driver_dir
    driver = webdriver.Chrome(chromedriver_dir)
    driver.get('https://www.asianacargo.com/tracking/viewTraceAirWaybill.do')
    wait = WebDriverWait(driver, 10)
    row_num = original_row_num
    for awb_num in list:
        # 브라우저가 나올때까지 대기 및 검색버튼 나오는지 확인 후 다음스탭 진행
        wait.until(EC.element_to_be_clickable((By.ID, 'btn_search')))
        driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div/input[2]').send_keys(awb_num[3:])
        track_button = driver.find_element_by_xpath('//*[@id="btn_search"]')
        track_button.click()
        # 수량/중량 text나오는지 검사
        chk_result = check_screen_result(driver, row_num, awb_num, ws)
        if chk_result == 'no':
            row_num+=1
            continue
        # Shipment History 찾아서 클릭
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="R'+awb_num+'"]/div/div/div[3]/div[1]/h4/a').click()
        # Shipment History 정보 가져오기 1-Booked pcs 수량 체크
        booked_pcs = check_pcs(driver, awb_num, 'BKD')
        # Shipment History 정보 가져오기 2-Departure pcs 수량 체크 만약 출발전이면 not yet departed 반환
        dept_pcs = check_pcs(driver, awb_num, 'DEP')
        arr_pcs = check_pcs(driver, awb_num, 'ARR')
        # Flight 상세정보 가져오기 3-STD, ATD, STA, ATA정보
        schedule_info = get_flight_info(driver, awb_num, dept_pcs, arr_pcs)
        STD = schedule_info[0]
        ATD = schedule_info[1]
        STA = schedule_info[2]
        ATA = schedule_info[3]
        ws.cell(row_num, 2).value = STD
        ws.cell(row_num, 3).value = ATD
        ws.cell(row_num, 4).value = STA
        ws.cell(row_num, 5).value = ATA
        remark = ""
        if dept_pcs == None:
            ''
        elif int(booked_pcs) > int(dept_pcs):
            remark += '파샬 건'
            ws.cell(row_num, 6).value = remark
        driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/div/input[2]').clear()
        time.sleep(0.1)
        row_num += 1
    print('아시아나 tracking 완료')
    driver.quit()
    return row_num