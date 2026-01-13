'''
mini script to warm up and count down days to new year
'''

from datetime import datetime

now = datetime.now()


new_years_day = datetime(year=now.year + 1, month=1, day=1)
difference = new_years_day - now
print(f"There are {difference.days} days and {int(difference.seconds / 60 /60)} hours left till 2027")