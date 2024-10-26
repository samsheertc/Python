#Usual Method to list 2 folders under current dir
import os
cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())  #List current_dir/Sample-Dir-One
os.chdir(cwd)

print(os.listdir())  #List current_dir/

cwd = os.getcwd()
os.chdir('Sample-Dir-Two') #List current_dir/Sample-Dir-Two
print(os.listdir())
os.chdir(cwd)





import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    ## Act as set-up for Context-Manager
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd) #Act as Tear Down for Context-Manager


with change_dir('Sample-Dir-One'):
    print(os.listdir())

with change_dir('Sample-Dir-Two'):
    print(os.listdir())
