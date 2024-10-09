try:
    f = open('curruptfile.txt')
    if f.name == 'currupt_file.txt':
        raise Exception
    var = bad_var
except FileNotFoundError as e:
    print('File Is Missing')
    print(e)         #System Generated Error
except IOError as e:
    print('First!')   #Custom Error
    print(e)         #System Generated Error
except Exception as e:
    print('Second')  #Custom Error
    print(e)         #System Generated Error
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
print('End of program')
