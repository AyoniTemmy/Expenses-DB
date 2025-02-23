print('Hello World')
print ('Snake eats')
print(8.9 + 7.8)
a= 600 + 800
j= 660 + 500
c = 700 + 700

print (a != j)

a = 9
b = 1

## bitwise operators
print (bin (a))

print (bin (b))
print (bin (a & b))
print (bin (a | b))

c = 8
print (bin (c))

print (bin (a & c))
print (bin (a | c))
print (bin (a ^ c))

print (bin (~ 10))

print (bin (25))
print (bin (30))

print (bin (180))

## lists
Adam_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'f', 'c', 'h']
print (Adam_list)

print (Adam_list[-5])
print (Adam_list[-12: -2])
print (Adam_list[7:])
print(Adam_list[3::])
print(Adam_list[3:])
print(Adam_list[::3])
print(Adam_list[-3:])

Adam_list.append('a')
print (Adam_list)

Adam_list.extend(['b', 'sand','2'])
print (Adam_list)

Sarah_list = [13, 23, 90]
Cole_list = Adam_list + Sarah_list
print (Cole_list)

hol_list =Cole_list[9:]*3
print(hol_list)

del Sarah_list

del hol_list[::3]
print(hol_list)

print(hol_list.pop())
print(hol_list)

# List Comprehension(creating a list by looping through another list)
kay_list = [x for x in hol_list if isinstance(x, str)]
print(kay_list)

#Membership test
print(0 not in kay_list)
print('2' in kay_list)

##Tuples
tuple_1 = ('ada', 1, 2, 3, 4, 5, ('grain', 'seed', 3), [7, 8, 0])
print(tuple_1)
print(type(tuple_1))

print(tuple_1[2])

Tai_list =list(tuple_1[1:6])
print(Tai_list)
print(type(Tai_list))

print(tuple_1.index(3))
tuple_1[-1].extend ([19, 10,11, "tail"])
print(tuple_1)

print(tuple_1.index(3))
tuple_1[-1].extend (Tai_list)
print(tuple_1)

print(Tai_list)

faith_list = ", ".join(map(str,tuple_1[-2]))

print(faith_list)

print(Tai_list)
print(tuple_1[-2])

##set
my_set1 = {1, 2, 3, 4, 5, 6, 0}
my_set2 = set([4, 6, 7, 9, 0])
my_set3 = {4, 6, 0}
my_set4 = frozenset([7,9,0,8])

print(my_set1)
print(my_set2)
print(my_set3)
print(my_set4)

my_set2.add(5)
print(my_set2)

popped = my_set2.pop()
print(my_set2)
print(popped)

my_newset = my_set3.copy()
print(my_newset)

my_set5 = my_set1|my_set2|my_set3|my_set4
print(my_set5)

print(my_set2.intersection(my_set3,my_set4))
print(my_set2.symmetric_difference(my_set4))
print(my_set2.isdisjoint(my_set4))

my_set3.remove(0)
print(my_set3)
print(my_set3.isdisjoint(my_set4))

print(my_set3.issubset(my_set1))
print(my_set1.issuperset(my_set3))


#Dictionary
My_dict1 = {'a':1, 'b':4, 'c':78, 'd':7}
print(My_dict1)
My_dict2 = dict({'n':80, 'f':6, 'h':90})
print(My_dict2)

My_dict1.pop('c')
print(My_dict1)
My_dict1.popitem()
print(My_dict1)

## Creating a dictionary by assigning a single value to the keys of the new dictionary
key1 = ('a', 'd', 'e')
my_dict3 = dict.fromkeys(key1, 10)
print(my_dict3)

##Creating a dictionary by assigning different values to the keys
key3 = ('ada', 'grace', 'victor', 'ade', 'funke')
values = [40, 60, 65, 84, 9]

## Method1: using a loop
mydict4 = {}
for i, key in enumerate(key3):
    mydict4[key] = values[i]
print(mydict4)

## Method 2: Using Dictionary comprehension
mydict5 = {key:value for key, value in zip(key3, values)}
print(mydict5)

##update a dictionary
mydict5.update({'i' : 67, 'j' :5})
print(mydict5)

## set a default value for a dictionary key

mydict5.setdefault('ice', 88)
print(mydict5)

##Conditional Statement


print(Adam_list)
del Adam_list[10:]
print(Adam_list)
Adam_list = [x / 2 for x in Adam_list]
print(Adam_list)

list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [x for x in list1 if isinstance(x,int) if x%2 == 0]
print(list2)

list3 = range(20)
list2 = [x for x in list3 if x % 2 == 0]
print(list2)

list4 = [i for i in range(1, 9) if i % 2 == 0]
print(list4)


print(mydict5)

print(mydict5.get('chim', 'not found'))

A = 100
B = 10
if A >= 10:
    if A > B:
        if A == 100:
            print('A is greater or equal to 10')
            print('A is less than B')
        else:
            print(f'A = {A}')
    