import numpy as np

#integer data !

i = 10 
print(type(i)) # will print the data type of i !

a_i = np.zeros(i, dtype=int) #declaring an array :D
print(type(a_i)) 
print(type(a_i[0])) #gives int64 as the number 0 is stored with 64 bit precision! :D

#floats!

x = 119.0
print(type(x))

#scientific !

y = 1.19e2
print(type(y)) 

z = np.zeros(i, dtype=np.float64)
print(type(z)) 
print(type(z[0]))