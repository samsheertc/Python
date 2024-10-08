#Writing Files:
##The Error:
with open("test.txt", "r") as f:
	f.write("Test")


#Writing Starts:
with open("test2.txt", "w") as f:
	pass

with open("test2.txt", "w") as f:
	f.write("Test")
	f.seek(0)
	f.write("Test")

with open("test2.txt", "w") as f:
	f.write("Test")
	f.seek(0)
	f.write("R")


#Copying Files:
with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)

#Copying the/your image:
##The Error
with open("bronx.jpg", "r") as rf:
	with open("bronx_copy.jpg", "w") as wf:
		for line in rf:
			wf.write(line)

##Copying the image starts, without chunks:
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		for line in rf:
			wf.write(line)

##Copying the image with chunks:
with open("bronx.jpg", "rb") as rf:
	with open("bronx_copy.jpg", "wb") as wf:
		chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
