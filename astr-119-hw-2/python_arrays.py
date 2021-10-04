x = [0.0, 3.0, 5.0, 2.5, 3.7] 
print(type(x))


#removing third element! :)

x.pop(2)
print(x)

#removing element with value = 2.5 ! :)

x.remove(2.5)
print(x)

x.append(1.2)
print(x)

#get a copy !

y = x.copy()
print(y)

# count the number of elements equal to 0 ! :D

print(y.count(0.0))

#print index of with value 3.7!

print(y.index(3.7))

#sort the list 
y[0] = 5.9
print(y)

#put things in ascending order! :D
y.sort()
print(y)

#put stuff in descending order! :D
y.reverse()
print(y)

#make y empty :( 
y.clear()
print(y)