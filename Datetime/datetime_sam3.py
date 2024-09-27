import datetime
import pytz

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = datetime.datetime.now()
#dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern')) #Error
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))
dt_str='September 26, 2024'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime
