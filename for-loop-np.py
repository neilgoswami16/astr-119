import numpy as np

def main():

    i = 0 # i is an integer
    n = 10 #another integer
    x = 119.0 #floating point number

    #use numpy to declare array 

    y = np.zeros(n, dtype=float)

    #use for loops 

    #changing value of numbers in y 
    for i in range(n): # i in range [o, n-1]
        y[i] = 2.0 * float(i) + 1.0

    #printing out all the values in y
    for y_element in y:
        print(y_element)

#execute main func
if __name__=="__main__":
    main()
