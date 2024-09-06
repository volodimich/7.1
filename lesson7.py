my_dict = {'vova': 2003, 'vlad': 2009, 'misha': 2016}
print(my_dict)
print(my_dict['vova'])
my_dict['Ostap'] = 1874 #
print(my_dict) # вывод отсутствующего значения в словаре без ошибки*
my_dict['sasha'] = 2001
my_dict['semen'] = 1987
print(my_dict)
a = my_dict.pop('semen')
print(a)
print(my_dict)
#множества
my_set = {0, 3, 2, '3', True, (1, 2)}
print(my_set)
my_set.add(4)
my_set.add(12)
my_set.discard(True)
print(my_set)