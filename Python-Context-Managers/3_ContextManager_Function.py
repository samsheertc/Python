
#### Using contextlib through a Function with Decorator ####

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f   # Act as set-up for Context Manager
    finally:
        f.close() # Act as a Teardown for Context Manager. Run after the f.write block below


with open_file('sample.txt', 'w') as f:
    f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit.')

print(f)        #<_io.TextIOWrapper name='sample.txt' mode='w' encoding='cp1252'>
print(f.closed) #True
