import datetime
import pytz

#DayLight Beginning
dt_central = datetime.datetime(2024,3,10,1,00,00)
central_tz = pytz.timezone('US/Central')
dt_central = central_tz.localize(dt_central)
dt_east = dt_central.astimezone(pytz.timezone('US/Eastern'))
print(f"Central Time {dt_central}\nEastern Time {dt_east}")

print("\n")
#DayLight Ending
dt_central = datetime.datetime(2024,11,3,1,00,00)
central_tz = pytz.timezone('US/Central')
dt_central = central_tz.localize(dt_central)
dt_east = dt_central.astimezone(pytz.timezone('US/Eastern'))
print(f"Central Time {dt_central}\nEastern Time {dt_east}")
