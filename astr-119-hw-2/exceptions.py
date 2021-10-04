
# use try when you think something might go wrong! :D

try:
    print(a)
except:
    print("a is not defined!")


#specific errors!!! :D

try:
    print(a) #will cause exception since a is undefined :-/
except NameError:
    print("a is still not defined")
except:
    print("Something else went wrong")

print(a)