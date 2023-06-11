import datetime
import time


def cal_time():
    # 生成当前日期, 样式为: 2022-07-15
    start_date = '2023-04-10'
    today_time = datetime.datetime.now().strftime("%Y-%m-%d")
    date1 = time.strptime(start_date, "%Y-%m-%d")
    date2 = time.strptime(today_time, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    return (date2 - date1).days
