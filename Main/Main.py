#first_module.py
def main():
    print("First Module's Name: {}".format(__name__))
if __name__ == '__main__':
    main()

#first_module.py
if __name__ == '__main__':
    print("Run Directly")
else:
    print("Run from Import")

#second_module.py
import first_module
print("Second Module's Name: {}".format(__name__))




#first_module.py
print("This will always be run")
def main():
print("First Module's Main Method")
if __name__ == '__main__':
    main()
    

#second_module.py
import first_module
first_module.main()
print("Second Module's Name: {}".format(__name__))
