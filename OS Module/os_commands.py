#----------------------------------------------------------------------------------------------------------------------------------------
import os
print(dir(os))                                                      #Check what methods exists
print(os.getcwd())                                                  #Get current working directory
os.chdir('C:/Users/samsh/Desktop')                                  #Change directory
print(os.getcwd())
os.listdir()                                                        #list directory and files in the current directory as LIST
os.listdir(<dir>)                                                   #list directory and files under the mentioned directory as LIST
os.mkdir('dir1')                                                    #Create a directory
os.mkdir('dir1/dir2/dir3')                                          #Error
os.makedirs('dir1/dir2/dir3')                                       #Make directories recursively
os.rmdir('dir1/dir2/dir3')                                          #Remove directory mentioned. Here only dir3
os.removedirs('dir1/dir2/dir3')                                     #Remove directory recursively. dir1, dir2 and dir3
os.rename('test.txt', 'demo.txt')                                   #Rename test.txt to demo.txt
#----------------------------------------------------------------------------------------------------------------------------------------
import os
os.stat('demo.txt')                                                 #Print all info of a file
import datetime
print(os.stat('Startup.sql').st_size)
print(os.stat('Startup.sql').st_mtime)
mode_time = os.stat('Startup.sql').st_mtime
print(f"{mode_time} -> {datetime.datetime.fromtimestamp(mode_time)}")
#---------------------------------------------------------------------------------------------------------------------------------------
#traverse directory recursively
#os.walk('path') is a generator that yields a tuple of three values
#For each directory that it sees it yields (directory path , directories with in that path, files with in that path)
#e.g: (main folder, [dir1, dir2, dir3], [file1, file2, file3])
	
for dirpath, dirnames, filenames in (os.walk('C:/Users/samsh/Desktop/')):
	print('-'*80)
	print('Current Path:', dirpath)
	print('Directories:', dirnames)
	print('Files:',filenames)
#----------------------------------------------------------------------------------------------------------------------------------------
os.environ                                                           #Get all ENVIRONMENT variables
print(os.environ)                                                    #Provides a dictionary of all env variables and values
print(os.environ.get('INFA_HOME'))
print(os.environ.get('SPARK_HOME'))
#----------------------------------------------------------------------------------------------------------------------------------------
os.path.join('path', 'file')                                         #Join path without worrying about

path = os.environ.get('SPARK_HOME')
print(path)                                                          #D:\spark-3.5.2
file_path = os.path.join(path, 'file.txt')
print(file_path)                                                     #D:\spark-3.5.2\file.txt

print(os.path.dirname('D:/spark-3.5.2/file.txt'))                    #D:/spark-3.5.2 - Get  (dirname
print(os.path.basename('D:/spark-3.5.2/file.txt'))                   #file.txt       - Get basename
print(os.path.split('D:/spark-3.5.2/file.txt'))                      #('D:/spark-3.5.2', 'file.txt') get (dirname, basename)

print(os.path.exists('D:/spark-3.5.2'))                              #check if the path exists or not
print(os.path.isdir('D:/spark-3.5.2'))                               #check if the Directory exist 
print(os.path.isfile('D:/spark-3.5.2/RELEASE'))                      #check if the file exist
print(os.path.splitext('D:/spark-3.5.2/file.txt'))                   #('D:/spark-3.5.2/file', '.txt')

print(dir(os.path))
#----------------------------------------------------------------------------------------------------------------------------------------
