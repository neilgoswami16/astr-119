import numpy as np
import sys

# define a func that returns value

def expo(x):
    return np.exp(x)


#define subroutine that does not return a value

def show_expo(n):
    for i in range(n):
        print(expo(float(i)))

#define a main func

def main():
    n = 10

    #checks is there is a command line argument! :D
    if(len(sys.argv)>1):
        n = int(sys.argv[1]) #if an arg is provided, use it for n 

    show_expo(n) 

#running the main function! :D

if __name__ == "__main__":
    main()


