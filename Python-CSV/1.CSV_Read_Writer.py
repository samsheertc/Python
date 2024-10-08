import csv

#Step1
#Read from names.csv file
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader) #<_csv.reader object at 0x0000018252755900>
    next(csv_reader)  #just to skip header
    for line in csv_reader:
        print(line[0]) #first_name
        print(line[1]) #last_name
        print(line[2]) #email
        print(line)
        print()

#Step2
#Read from names.csv and write to a new_names.csv file as a tab delimted file
with open('names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	with open('new_names.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file, delimiter='\t')
		#delimiter='\t',lineterminator='\r',  quoting= 1
		for line in csv_reader:
			csv_writer.writerow(line)

#Read Step-2 file with out a Delimeter
with open('new_names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)
	for line in csv_reader:
			print(line)

#Read Step-2 file with  tab Delimeter
with open('new_names.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter='\t')
	for line in csv_reader:
			print(line)
