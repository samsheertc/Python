print('Imported my_module Successfully...')
test = 'Test String'

def find_index(target, to_search):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(target):
        if value == to_search:
            return i

    return -1
