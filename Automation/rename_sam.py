import os
os.chdir('C:/Users/samsh/Google Drive/US_Visa_Photos/Image')

for f in os.listdir():
	if f == '.DS_Store' or f == 'desktop.ini' :
		continue
	print(os.path.splitext(f))
	file_name, file_ext = os.path.splitext(f)
	print(file_name)
	print(file_ext)

	print(file_name.split('-'))
	f_title, f_course, f_number = file_name.split('-')
	f_title = f_title.strip()
	f_course = f_course.strip()
	f_number = f_number.strip()[1:].zfill(2)
	print(f_title)
	print(f_course)
	print(f_number)

	new_name = f'{f_number}-{f_title}{file_ext}'
	print(new_name)
	print('*'*50)
	#os.rename(f, new_name)

