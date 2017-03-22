list_1 = [9, 19, 'a']
dict_1 = {'a':1, 'b':2, 'c':3}
set_1  = {'a', 'b', 'c'}

#ADD
list_1.append(29)
list_1.insert(0, 'b')
list_1 + [39]
list_1.extend([49, 59, 69])
list_1 + [79,89]

dict_1['d'] = 4

set1.add('d')
set1.update([1,2,3], {4,5,6})


#DELETE
del list_1[1:3] 
del list_1[4]
del list_1
list_1.remove(29)
list_1.pop(1) # return the deleted value
list_1.pop() # remove the last index
list_1.clear()
list_1[1:4] = []

dict_1.pop('a')
del dict_1['b']
dict_1.clear()
del dict_1

set_1.discard(2) 
set_1.remove(2) # throw error
set_1.pop() # take no arguments, random remove, return remove value
set_1.clear()


#MODIFY
list_1[0] = 'b'
list_1[-5:-1] = [99,119,129]

dict_1['a'] = 11


#SERCH
list_1[0]
list_1[-5:-1]

dict_1.get('a') 
dict_1['a']
