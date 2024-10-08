my_tup1 = ('key1', 'value1')
my_tup2 = ('key2', 'value2')

my_list1 = ['key1', 'value1']
my_list2 = ['key2', 'value2']

my_dict = dict([my_tup1, my_tup2])
print()
print(f'Tuple to dictionary\n{my_tup1}\n{my_tup2}\n{my_dict}\n')
print(f'Tuple to set  \n{my_tup1} \n{set(my_tup1)}\n')
print(f'List  to set  \n{my_list1}\n{set(my_list1)}\n')
print(f'Tuple to list \n{my_tup1} \n{list(my_tup1)}\n')
print(f'List to tuple \n{my_list1}\n{tuple(my_list1)}\n')
