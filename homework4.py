#immutable_var=1, 3, 5, 'apple', 'banana'
#print(immutable_var)
#print(type(immutable_var))
#immutable_var[0]=7 #неизменяемы тип данных, можно заменить стороку, но нельзя заменить часть кортежа
mutable_list=['apple', 1, 3, 5, 'banana']
print(mutable_list)
mutable_list[0]='lemon'
print(mutable_list)
mutable_list[2]='potato'
print(mutable_list)