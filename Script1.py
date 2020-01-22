# -*- coding: utf-8 -*-
"""
Spyder Editor
Name Brenna

This is a temporary script file.
"""

#The first command you learn is always:
print (' hello world ' )
#Actually, that's not quite right, its really:
print ("Hello World!")
#You can do math too.
print ('21 + 21') 
#And you can mix and match words and math.

print 'The answer to life, the universe and everything is' , (21+21)

"""So far every command we performed used un-addressed parts of memory, so we can't find the variables again. If you want to store a value and be able to retrieve it, you need to define a variable. In python, that is super easy:
"""

a = 12

#If you want to know what 'a' is, you can check the variable explorer, or you can ask python.


print (a)
#And you can then use your variable in a command.

print (a+a)

#Datatypes: this is biggie. 'a' can be a whole bunch of different types of data. Its important for the computer to know what type, so it can properly represent it with a number. A can be a string (text):
a = '12'

print (a+a)

#Adding two strings together in python means put the two strings together, this will become useful I promise.
#'a' can be an integer:

a = 12
#Math with integers is tricky...
print (a/7)
#'a' can be a float: (the period at the end of the number tells python is a floating number)

a = 12.

print (a/7)

#'a' can be a list of any of those basic datatypes. A list is defined with square brackets (bracket types are important in python), with elements separated by commas.

a = [1.,2.,3.,4.]
#You can retrive parts of this list by indexing the list. The first element is zero in python:

print a[0]

#Each element in a list can be used like a variable.

print a[1]+a[2]

#Another useful dataype is dictionary. A dictionary has keys which point to a variable. The variable can be any type, and it is accessed by the key. A dictionary has curly brackets.

d = {'a':[1.,2.,3.],'b':['1','2','3']}
#You access variables in a dictionary by their key:

print d['a']

#Which returns a list, which can then be accessed.

print d['a'][2]+d['a'][1]

"""One of the amazing things of python is the amount of libraries people write to add functionality. Libraries are tools or pieces of code which do useful things that you get use, and you don't have to write from scratch. The two fundamental libraries for scientific computing with python are Numpy and Scipy.

To import numpy - a library full of useful numerical math tools we execute:"""


import numpy as np

"""The line imports the numpy library, and all its tools. Because we are lazy and don't want to type numpy everytime, we tell python to nickname numpy - np for now.

Numpy arrays are the backbone datatype for scientific computing. An array is basically a wrapper of a list or a list of lists. Numpy arrays can have lots of dimensions. For now we'll work with one dimensional arrays.

To create a 1-d array with the same elements as our list 'a' we could write:"""

aa = np.array([1.,2.,3.,4.])

#You access or 'index' array elements in the same way as a list:

print aa[0]

#But array operations are much different than list operations.
#Adding two lists, concatenates the lists together:

print (a+a)

#Adding two arrays, adds each element, element wise:

print aa+aa

"""Basically any operator is available for elementwise operation on numpy arrays. This might not sound cool to you right now, but trust me, its awesome.

For example, the area weighted average precipitation across a basin is given by the following formula:

Pavg=∑n0PiAi∑n0Ai 
say I need to multiply a bunch of different areas and precipitation heights together to calculate a volume of water.

I can do all the operations like this:"""

precip = np.array([4.0,4.5,5.3,6.0,2.2,3.0])
area = np.array([100.,300.,50.,25,700.,1000.])
volumes = precip*area
print volumes


#if I want to get the total precipitation then I need to add all these volumes together. Numpy has an answer for that.
#Sum the precipitation:

v_t = np.sum(volumes)
print v_t


#If I want to calculate the area weighted average precipitation, I would need to divide by the total area.

p_avg = v_t/np.sum(area)
print p_avg

#And the ultra pythonic way it combine all the operations into one line:

p_avg2 = np.sum(precip*area)/np.sum(area)
print p_avg2

#A super useful command is 'len'. len tells us how long an array or list or dictionary is:

len(precip)

#That's probably not amazing to you, but a low level language like C would require 'for' loops to do all of these operations. A 'for loop' is a basic element of code it basically says: for this many times do these things.

#A python for loop to print all values of precipitation would look like this:
    
for i in xrange(len(precip)):
    print precip[i]

#This command says i = 0,1,2,3,4,5 print precip[i].
#A for loop to calculate the area weighted average precipitation is:
    
v_t = 0
a_t = 0
for i in xrange(len(precip)):
    v_i = precip[i]*area[i]
    v_t = v_t + v_i
    a_t = a_t + area[i]
    
p_avg = v_t/a_t
print p_avg

#his is the end of script 1. I would like all commands and comments turned in as part of this script.





















