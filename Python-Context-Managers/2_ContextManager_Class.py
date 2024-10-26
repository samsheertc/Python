#Context Manager through a class
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    #Act as a set-up method for Context Manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # Act as a Teardown method for Context Manager
    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'w') as f:
    f.write('Testing Class')

print(f)        #<_io.TextIOWrapper name='sample.txt' mode='w' encoding='cp1252'>
print(f.closed) #True
