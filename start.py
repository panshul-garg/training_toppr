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

pi_tuple = (1,3,'hello world')
new_tuple= list(pi_tuple)
new_list=tuple(new_tuple)
#print (pi_tuple)
#print (new_tuple)
#print (new_list)
#print(len(pi_tuple)) 
#print(max(new_tuple)) 
#print(min(new_tuple))
new_dict={1:0,2:5,'a1':'b1',1:'b1'}
#print (new_dict)
#print (new_dict[1])
#pi_tuple[2]=5
keys=new_dict.keys()
values=new_dict.values()
#print (keys)
#print (values)

if len(pi_tuple)>4:
	print("len>4")
elif len(pi_tuple)==4:
	print("len=4")
else:
	#print("len<4")
	pass


for i in range(len(pi_tuple)):
	pass
	#print(pi_tuple[i])
for i in new_dict:
	pass
	#print (str(i)+' '+str(new_dict[i]))

i=0
while(i<=20):
	if i%2==0 :
		#print i
		break
	i+=1

def func1(dict):
	dict[1]=55


i=5
#print new_dict
func1(new_dict)
#print new_dict


test_file =open("Commands","r+")
#print(test_file.mode)
#print(test_file.name)
read_file=test_file.read()
#print (read_file)

class Animal:
	#__name=None
	height=0
	__sound=0
	__weight=0

	def __init__(self,name,h,w,s):
		self.__name=name
		self.height=h
		sound=s
		__weight=w
	def set_name(self,name):
		self.__name=name
	def get_name(self):
		return self.__name

	def __str__(self):
		return ('{} = name {} =weight {}=height {}=sound'.format(self.__name,self.__weight,self.height,self.__sound))

animal = Animal('hello',5,25,'bulla')
print (animal.get_name())
print (animal)


class Dog(Animal):
	owner=""
	def __init__(self,name,owner,height,weight,sound):
		self.owner=owner
		super().__init__(name,height,weight,sound)

	def get_name(self):
		return self.owner

#dog=Dog('jacky','panshul','50','25','bark')


