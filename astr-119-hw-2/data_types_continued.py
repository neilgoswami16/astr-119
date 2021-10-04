#string!

s = "I am a string"
print(type(s))

#Boolean!
yes = True
print(type(yes)) 

no = False
print(type(no))

#List -- ordered and changeable! :D

alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple! :)

alpha_tuple = ("a", "b", "c")

try:
    alpha_tuple[2] = "d"
except TypeError:
    print("We cant change elements of a tuple.")

print(alpha_tuple)


