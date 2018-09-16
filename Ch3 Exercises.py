#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:25:04 2018

@author: alexanderbayers
"""


'''
first_var = 4
second_var = 3.1415
third_var = 1.0
fourth_var = 2+4j
fifth_var = 'Hello'
sixth_var = 'World'

print(type(first_var))
print(type(second_var))
print(type(third_var))
print(type(fourth_var))
print(type(fifth_var))
print(type(sixth_var))

var_list = [first_var, second_var, third_var, fourth_var, fifth_var, sixth_var]

for counter in range(len(var_list)-1):
    for new_counter in range(counter+1, len(var_list)):
        try:
            test = (var_list[counter]/ var_list[new_counter])
            print(type(var_list[counter]), type(var_list[new_counter]))
        except:
            pass


ex = 'Python is an interesting and useful language for numerical computing!'
print(ex[0:6])
print(ex[-10:-1])
print(ex[13:15])
print(ex[::-1])
print(ex[::2])


x = [[1, .5], [.5, 1]]
y = x
y[0][0] = 1.61


print(x)
z = x[:]
y[0][0] = 1j
print(id(x))
print(id(y))
print(id(z))

print(id(x[0]))
print(id(y[0]))
print(id(z[0]))


Prblem 10
Use copy.deepcopy
'''

mylist = [4, 3.1415, 1.0, 2+4j, 'Hello', 'World']
print(mylist)
#del(mylist[2])
#mylist.remove(1)
#print(mylist)
mylist.extend([1.0, 2+4j, 'Hello'])
#print(mylist)
#print(mylist[::-1])
#print(mylist.count('Hello'))
myset = set(mylist)
print(myset)