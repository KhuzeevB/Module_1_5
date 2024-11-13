immutable_var = 1,2,'a','b'
print("Immutable tuple: ",immutable_var)
#immutable_var[0]=5
#print(immutable_var) не можем изменить элемент кортежа т.к. мы создали список и необходимо сохранить в неизменом виде.
mutable_list=[1,2,'a','b']
mutable_list.append('Modifield')
print("Mutable list: ",mutable_list)






