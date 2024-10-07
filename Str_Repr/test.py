a = [1,2,3,4]
b = 'sample string'

print(str(a))   #[1, 2, 3, 4]

print(repr(a))  #[1, 2, 3, 4]

print(str(b))  #sample string

print(repr(b)) #'sample string'




import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))    #str(a): 2024-10-07 16:29:58.341528+00:00

print('str(b): {}'.format(str(b)))    #str(b): 2024-10-07 16:29:58.341528+00:00

print()

print('repr(a): {}'.format(repr(a)))  #repr(a): datetime.datetime(2024, 10, 7, 16, 29, 58, 341528, tzinfo=<UTC>)

print('repr(b): {}'.format(repr(b)))  #repr(b): '2024-10-07 16:29:58.341528+00:00'

print()

