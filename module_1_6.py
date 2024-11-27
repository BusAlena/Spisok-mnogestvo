my_dict= {'Юлия':1987, 'Алена':1985, 'Катерина':1979, 'Владимир':1984}
print(my_dict)
print(my_dict.get('Алена'))
print(my_dict.get('Максим'))
my_dict.update({'Ольга':1959, 'Михаил':1960})
a=my_dict.pop('Михаил')
print(a)
print(my_dict)
#Работа с множествами:
my_set={1, 'Юлия', 3.14, 1, 12, 3.14}
print(my_set)
my_set.update({45, 753})
print(my_set)
s=my_set.remove('Юлия')
print(my_set)