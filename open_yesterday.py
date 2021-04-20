def create_yesterday_str():
    day = (date.today() - timedelta(1))
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    day_iso = day.isoformat().replace('-', '')
    dayname = weekDays[day.weekday()]
    date_format = f'{day_iso}_{dayname}'
    return date_format

# create_yesterday_str()

if __name__ == '__main__':

    import os
    from datetime import date, timedelta

    yesterday = f'./OneDrive - Timextender A S/_daily/{create_yesterday_str()}_.txt'
    print(yesterday)
    os.system(f'notepad {yesterday}')