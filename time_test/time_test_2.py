import schedule
import time
from datetime import datetime
import sample_run



def job():
    print("I'm working...")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    sample_run.run_hi()

# schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":10").do(job)
# schedule.every().minute.at(":20").do(job)
# schedule.every().minute.at(":30").do(job)
# schedule.every().minute.at(":40").do(job)
# schedule.every().minute.at(":50").do(job)

schedule.every(10).seconds.do(job)
schedule.every().minute.at(":10").do(sample_run.run_say)
schedule.every(30).seconds.do(job)
while True:
    schedule.run_pending()

    time.sleep(1)