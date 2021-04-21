import os
from datetime import date, timedelta

def create_prev_day_str(daily_dir = './OneDrive - Timextender A S/_daily/'):
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    tday = date.today()
    if tday.weekday() == 0:
        prev_day = tday - timedelta(3)
    else:
        prev_day = tday - timedelta(1)
    day_iso = prev_day.isoformat().replace('-', '')
    dayname = weekDays[prev_day.weekday()]
    date_format = f'{day_iso}_{dayname}'
    return date_format

if __name__ == '__main__':

    import os
    from datetime import date, timedelta

    prev_day = f'./OneDrive - Timextender A S/_daily/{create_prev_day_str()}_.txt'
    print(prev_day)
    os.system(f'notepad {prev_day}')