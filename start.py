import random
import sys
import os

#print ("Hello World")

#Comment

'''
Multiline Comment
'''

name='Panshul'
#print(name)

#Number Strings Lists Tuples Dictionaries
#+ - * / % ** //
quote= "\" this is a quote\""

multiline = ''' Hello
World
kjc'''
#print ("%s %s %s" %('this is a string','another string',quote),end="")
#print (multiline)

random_list=['r0','r1','r2','r3','r4','r5']
#print (random_list[0])
random_list[0]='R0'

#print (random_list[0])
#print(random_list[1:3])

other_list=['o0','o1','o2','o3']

new_list=[random_list,other_list]
#print (new_list)
#print (new_list[0])
#print (new_list[1][2])
random_list.insert(2,'r0')
random_list.reverse()
random_list.sort()
#print(random_list)

new_list1=random_list+other_list
#print(new_list1)


# Tuples

pi_tuple = (1,2,3,'hello world')
new_tuple= list(pi_tuple)
new_list=tuple(new_tuple)
print (pi_tuple)
print (new_tuple)
print (new_list)
print(len(pi_tuple)) 
#print(max(new_tuple)) 
print(min(new_tuple))