import datetime
import pytz

###### localize a timestmap ######
ts = timestamp value of a location with out TZ
tz = timezone value of that location
tz.localize(ts)
timezone.localize(timestamp with out TZ)

#eg
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)


#Convert From Mountain time to Eastern
#dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern')) #Error
print(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)




dt_Easten = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))          #[Current time in Eastern Area]
dt_Central = datetime.datetime.now(tz=pytz.timezone('US/Central'))         #[Current time in Central Area]
dt_Mountain = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))       #[Current time in Mountain Area]
dt_Pacific = datetime.datetime.now(tz=pytz.timezone('US/Pacific'))         #[Current time in Pacific Area]
dt_India = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))         #[Current time in India]

print(dt_Easten)               #2024-09-26 23:26:10.314716-04:00
print(dt_Central)              #2024-09-26 22:26:10.315714-05:00
print(dt_Mountain)             #2024-09-26 21:26:10.315714-06:00
print(dt_Pacific)              #2024-09-26 20:26:10.316711-07:00
print({dt_India})              #

print(dt_Easten.isoformat())   #2024-09-26T23:26:10.314716-04:00
print(dt_Central.isoformat())  #2024-09-26T22:26:10.315714-05:00
print(dt_Mountain.isoformat()) #2024-09-26T21:26:10.315714-06:00
print(dt_Pacific.isoformat())  #2024-09-26T20:26:10.316711-07:00
print(dt_India.isoformat())    # 


#Convert using strftime
print(dt_mtn.strftime('%B %d, %Y'))   #September 26, 2024

#Convert using strptime
dt_str='September 26, 2024'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)                             #2024-09-26 00:00:00

# strftime - Datetime to String
# strptime - String to Datetime
