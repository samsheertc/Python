#----------------------------------------------------------------------------------------------------------------
dt_today = datetime.datetime.today()   #today() returns current local date time with a timezone of None.
dt_now = datetime.datetime.now()       #now() provides an option to pass in a timezone.
dt_utcnow = datetime.datetime.utcnow() #utcnow() provide UTC time but tzinfo is set to None

print(dt_today)  #2024-09-26 20:09:20.121120 #Local Time
print(dt_now)    #2024-09-26 20:09:20.121120 #Local Time
print(dt_utcnow) #2024-09-27 00:09:20.121120 #UTC Time
#----------------------------------------------------------------------------------------------------------------
import datetime
import pytz

dtc = datetime.datetime(2016,7,26,12,30,45,tzinfo=pytz.UTC)      #Convert a Datetime value to TimeZone
dt_now = datetime.datetime.now(tz=pytz.UTC)                      #Current UTC Time
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)  #Current UTC Time ..Alternate method
print(dtc)       #2016-07-26 12:30:45+00:00 
print(dt_now)    #2024-09-27 00:20:57.427277+00:00
print(dt_utcnow) #2024-09-27 00:20:57.427277+00:00


#Conversion from UTC to Other
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)                     #Current UTC Time
dt_india = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))     #Current Indian Time
dt_eastern = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))     #Current Eastern Time
dt_central = dt_utcnow.astimezone(pytz.timezone('US/Central'))     #Current Central Time
dt_moutain = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))    #Current Mountain Time
dt_pacific = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))     #Current Pacific Time
dt_India = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')) #[Current time in India]

print(f"Indian Time {dt_india}")       #2024-09-27 05:55:36.186811+05:30
print(f"UTC Time {dt_utcnow}")         #2024-09-27 00:25:36.186811+00:00
print(f"Eastern Time {dt_eastern}")    #2024-09-26 20:25:36.186811-04:00
print(f"Central Time {dt_central}")    #2024-09-26 19:25:36.186811-05:00
print(f"Mountain Time {dt_moutain}")   #2024-09-26 18:25:36.186811-06:00
print(f"Pacific Time {dt_pacific}")    #2024-09-26 17:25:36.186811-07:00
print(f"Indian Time {dt_India}")       #

#----------------------------------------------------------------------------------------------------------------
