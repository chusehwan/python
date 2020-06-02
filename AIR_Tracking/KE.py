from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹사이트 변수 정의
KE_URL = 'https://cargo.koreanair.com/ko/tracking'
# xpath & elements 주소 정의
MAWB_input = '//*[@id="awbDocNo1"]'
search_button = "//button[@type='button'][@class='btn btn-primary btn-block']"
more_status = 'viewAllBtn'
pol_etd_address = '//*[@id="myTabContent"]/div/div[2]/div/div/div[2]/div[3]'
pod_eta_address = '//*[@id="myTabContent"]/div/div[4]/div/div/div[2]/div[3]'


def check_status_more(driver):
    """웹페이지 상 status 항목이 밑으로 더 있을 때 모든상태보기 버튼이 있는지여부 검토 후 있으면 클릭"""
    try:
        time.sleep(0.3)
        more_status_botton = driver.find_element_by_class_name(more_status)
        time.sleep(0.3)
        more_status_botton.send_keys('\n')
    except:
        pass


def check_status_value(status_list, status, list_1, list_2):
    """status 정보 바탕 receive, departure등 정보 뽑아내기"""
    for i in status_list:
        if status in i.text:
            divided_received_info = i.text.split()
            if list_2 == "":
                return divided_received_info[list_1]
                break
            else:
                # date+month+time+minute 반환 ex) 29MAY03:34
                date = divided_received_info[list_2] + " " + divided_received_info[list_1]
                return date
                break
    return None


def convert_ke_time_info(value):
    """대한항공 트래킹 웹사이트에서 복사된 일자값을 통일된 양식(2020-05-20 18:00)으로 가공"""
    value = value
    month_dic = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
                 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    month_info = month_dic[value[3:6]]
    date_info = value[:2]
    time_info = value[6:]
    result = '2020-' + month_info + '-' + date_info + ' ' + time_info
    # 크롤링된 값 공통 값으로 정리하기(ex) 24 Mar 2020 18:00 -> 2020-03-24 18:00)
    return result


def get_tracking_info_ke(list, driver_dir, row_num, ws):
    """대한항공 홈페이지 접속 및 트랙킹 작업 awb list 바탕 진행"""
    ke_len = len(list)
    ws = ws
    chromedriver_dir = driver_dir
    driver = webdriver.Chrome(chromedriver_dir)
    driver.get(KE_URL)
    wait = WebDriverWait(driver, 10)
    row_num = row_num
    for awb_num in list:
        # 브라우저가 나올때까지 대기 및 검색버튼 나오는지 확인 후 다음스탭 진행
        wait.until(EC.element_to_be_clickable((By.ID, 'awbDocNo1')))
        # MAWB 입력
        driver.find_element_by_xpath(MAWB_input).send_keys(awb_num[3:])
        # 추적버튼 찾아서 클릭
        track_button = driver.find_element_by_xpath(search_button)
        track_button.click()
        # 빌넘버/구간 text나오는지 검사
        wait.until(EC.element_to_be_clickable((By.ID, 'tabClick')))
        # status 관련 정보가 더 있을 경우 '모든상태보기'버튼 눌러주기, 없으면 패스~
        check_status_more(driver)
        # 결과물 정보 파싱해오기
        status_list = driver.find_elements_by_class_name('statusItems')
        # 만약 검색결과가 없을 시 추가 절차 생략 및 remark란에 no_data기입 후 다음 AWB조회
        if len(status_list) == 0:
            ws.cell(row_num, 6).value ='No_data'
            driver.find_element_by_xpath('//*[@id="awbDocNo1"]').clear()
            print(awb_num, 'has no data')
            row_num += 1
            continue
        # Booked 값이 있으면 해당 값(편명) 반환, 없으면 None반환
        booked_flight_info = check_status_value(status_list, status='Booked', list_1=2, list_2="")
        if booked_flight_info != None:
            booked_flight = booked_flight_info.split('|')[1]
        # recevied pcs 값이 있으면 해당 값 반환, 없으면 None반환
        received_pcs = check_status_value(status_list, status='Received', list_1=1, list_2="")
        # pcs값이 천단위 이상일 시 콤마 삭제하여 나중에 int형으로 변환하기 쉽게 함
        if received_pcs != None and ',' in received_pcs:
            received_pcs = received_pcs.replace(',', '')
        # 출발시 pcs 값 반환, 없으면 None반환
        departure_pcs = check_status_value(status_list, status='Departed', list_1=1, list_2="")
        if departure_pcs != None and ',' in departure_pcs:
            departure_pcs = departure_pcs.replace(',', '')
        departure_flight_info = check_status_value(status_list, status='Departed', list_1=2, list_2="")
        if departure_flight_info != None:
            departure_flight = departure_flight_info.split('|')[1]
        # 출발했으면 시간 반환, 안했으면 None반환
        pol_atd = check_status_value(status_list, status='Departed', list_1=-1, list_2=-2)
        # 도착했으면 시간 반환, 안했으면 None반환
        pod_ata = check_status_value(status_list, status='Arrived', list_1=-1, list_2=-2)
        pol_etd = driver.find_element_by_xpath(pol_etd_address)
        pod_eta = driver.find_element_by_xpath(pod_eta_address)

        """위에서 확인된 부킹 pcs, received pcs, 부킹 편명, 출발 편명, status상 출발, 도착일정, 그래프상 일정 비교 하여 
            워크시트상 값 입력"""
        # POL ETD 정보 입력(POL ATD가 있으면 입력안함)
        remark = ''
        if pol_atd == None:
            ws.cell(row_num, 2).value = convert_ke_time_info(pol_etd.text)
        elif pol_atd != None:
            ws.cell(row_num, 3).value = convert_ke_time_info(pol_atd)
            if int(received_pcs) > int(departure_pcs):
                remark += '파샬 건 '
            if booked_flight != departure_flight:
                remark += '편명 변경건'
            ws.cell(row_num, 6).value = remark
        if pod_ata == None:
            ws.cell(row_num, 4).value = convert_ke_time_info(pod_eta.text)
        elif pod_ata != None:
            ws.cell(row_num, 5).value = convert_ke_time_info(pod_ata)

        driver.find_element_by_xpath('//*[@id="awbDocNo1"]').clear()
        time.sleep(0.1)
        row_num += 1
    print('대한항공 tracking 완료')
    driver.quit()
    return row_num
