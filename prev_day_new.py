import os

def create_day_iso():
    day = date.today()
    day_iso = day.isoformat().replace('-', '')
    return day_iso

daily_files = os.listdir('./OneDrive - Timextender A S/_daily')
actual_days = [f[:-5] for f in daily_files if f[:4] == '2021' and f[-5:] == '_.txt']
daily_files = [f for f in daily_files if f[:4] == '2021' and f[-5:] == '_.txt']
print(actual_days)
print()

prev_day == ''

for i in range(1,10):
#     print(i)
    date_try = str(int('20210426') - i) #str(int(create_day_iso()) - i)
#     print(date_try)
    try:
        prev_day = actual_days[int([i for i, s in enumerate(actual_days) if date_try in s][0])]
        print(f'{prev_day} is prev day')
        print(f'len is {len(prev_day)}')
        break
    except:
        print(f"{date_try} isn't a file found")
        continue
#         if prev_day == '':
#             continue
#         else:
#             break
#             print(prev_day)