import datetime
#----------------------------------------------------------------------------------------------------------------
############### datetime.date ###############
# Naive
d = datetime.date(2024, 9, 26)
print(d)                          #2024-09-26

tday = datetime.date.today()
print(tday)                       #2024-09-26
print(tday.year)                  #2024
print(tday.day)                   #26
print(tday.weekday())             #3 [day is thursday]
print(tday.isoweekday())          #4 [day is thursday]
                                  # weekday() - Monday is 0 and Sunday is 6
                                  # isoweekday() - Monday is 1 and Sunday is 7

#----------------------------------------------------------------------------------------------------------------
############### datetime.timedelta ###############
tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday+tdelta) #2024-10-03 [One week Later]
print(tday-tdelta) #2024-09-19 [One Week Ago]

#date2     = date1 [+ -] timedelta
#timedelta = date1 [+ -] date2

bday = datetime.date(2024, 10, 31)
till_bday = bday - tday

print(till_bday)                 #35 days, 0:00:00
print(till_bday.days)            #35
print(till_bday.total_seconds()) #3024000

#----------------------------------------------------------------------------------------------------------------
################ datetime.time ################ 
t  = datetime.time(9,30,45,100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)

#----------------------------------------------------------------------------------------------------------------
################ datetime.datetime ################ 
dt = datetime.datetime(2016,7,26,12,30,45,100000)
print(dt)        #2016-07-26 12:30:45.100000
print(dt.date()) #2016-07-26
print(dt.time()) #12:30:45.100000
print(dt.year)   #2016
print(dt.month)  #7
print(dt.day)    #26
print(dt.hour)   #12
print(dt.minute) #30
print(dt.second) #45

tdelta = datetime.timedelta(days=7)
print(dt+tdelta) #2016-08-02 12:30:45.100000

tdelta = datetime.timedelta(hours=12)
print(dt+tdelta) #2016-07-27 00:30:45.100000
#----------------------------------------------------------------------------------------------------------------


