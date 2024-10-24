#Suppose the my_module.py is moved to new location let say to "C:\Users\samsh\Desktop"
import sys 
print(sys.path) #Current Path the Python Looks for 
'''
[
'C:\\Users\\samsh\\My Drive (samsheer.tcp@gmail.com)\\PySpark\\PycharmProjects\\PySpark_Mac',
'C:\\Users\\samsh\\My Drive (samsheer.tcp@gmail.com)\\PySpark\\PycharmProjects',
'D:\\spark-3.5.2\\python', 'D:\\spark-3.5.2\\python\\lib\\py4j-0.10.9.7-src.zip', 
'C:\\Users\\samsh\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',
'C:\\Users\\samsh\\AppData\\Local\\Programs\\Python\\Python310\\DLLs',
'C:\\Users\\samsh\\AppData\\Local\\Programs\\Python\\Python310\\lib',
'C:\\Users\\samsh\\AppData\\Local\\Programs\\Python\\Python310',
'C:\\Users\\samsh\\My Drive (samsheer.tcp@gmail.com)\\PySpark\\PycharmProjects\\.venv',
'C:\\Users\\samsh\\My Drive (samsheer.tcp@gmail.com)\\PySpark\\PycharmProjects\\.venv\\lib\\site-packages'
]
'''

#We need to add the location of my_module.py as below
#Option-1
import sys
sys.path.append('C:\\Users\\samsh\\Desktop')
<Add Code>

#Option-2
#Add the location C:\Users\samsh\Desktop in  PYTHONPATH
import my_module
<Add Code>

Enter this in Terminal After Step2
import my_module
import sys
print(sys.path)


Import Modules
import random 
#to pull random values from a list
random.choice(LIST)

import math
rads=math.radians(90)
print(rads)
print(math.sin(rads))

import datetime
import calendar
today=datetime.date.today()
print(today)
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)
