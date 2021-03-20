import schedule
import time


def job():
    print("I'm working...")
def job2():
    print("I'm working2...")
def job3():
    print("I'm working3...")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


schedule.every(10).minutes.do(job)
schedule.every(5).seconds.do(job3)
schedule.every().hour.do(job)
schedule.every().day.at("23:05").do(job2)
schedule.every(5).to(10).days.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)