#----------------------------------------------------------------------------------------------------------------
dt_today = datetime.datetime.today()   #today() returns current local date time with a timezone of None.
dt_now = datetime.datetime.now()       #now() provides an option to pass in a timezone.
dt_utcnow = datetime.datetime.utcnow() #utcnow() provide UTC time but tzinfo is set to None

print(dt_today)  #2024-09-26 20:09:20.121120
print(dt_now)    #2024-09-26 20:09:20.121120
print(dt_utcnow) #2024-09-27 00:09:20.121120
#----------------------------------------------------------------------------------------------------------------
import datetime
import pytz

#Add timezone to a Date value
dtc = datetime.datetime(2016,7,26,12,30,45,tzinfo=pytz.UTC)
print(dtc)

#Current UTC Time
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now) #2024-09-27 00:20:57.427277+00:00


#Current UTC Time [Alternate method]
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow) #2024-09-27 00:20:57.427277+00:00


#Conversion from One timezone to Other
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)
#2024-09-27 00:25:36.186811+00:00 [Pull Current UTC Time]

dt_east = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
#2024-09-26 20:25:36.186811-04:00 [Convert Current UTC Time to Eastern Time]

dt_ctrl = dt_utcnow.astimezone(pytz.timezone('US/Central'))
print(dt_ctrl)
#2024-09-26 19:25:36.186811-05:00 [Convert Current UTC Time to Central Time]

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
#2024-09-26 18:25:36.186811-06:00 [Convert Current UTC Time to Mountain Time]

dt_pac = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))
print(dt_pac)
#2024-09-26 17:25:36.186811-07:00 [Convert Current UTC Time to Pacific Time]

dt_ind = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ind)
#2024-09-27 05:55:36.186811+05:30 [Convert Current UTC Time to Indian Time]
#----------------------------------------------------------------------------------------------------------------
