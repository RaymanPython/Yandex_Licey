import datetime

гimport schedule

i = 1


def job():
    global i
    print(f"Запустился {i} раз")
    i += 1
    print(datetime.datetime.now())


schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()