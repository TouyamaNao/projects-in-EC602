# white a python program that :
#     reads two integers X and Y using input()
#     calculates Z = X! - Y!

from math import factorial

X = int(input("Please input integer X:"))
while(X<0):
    X = int(input("X should be non-negative integer, please input again:"))

Y = int(input("Please input integer Y:"))
while(Y<0):
    Y = int(input("Y should be non-negative integer, please input again:"))

Z = int(factorial(X) - factorial(Y))
print(Z)

def getNumOfDec(A):
    i = 0
    if(A == 0):
        return 1
    X = abs(A)
    while True:
        X = X/10
        i = i + 1
        if (X==0):
            break
    return i

ZDecLength = getNumOfDec(Z)
print(ZDecLength)

def getNumOfBytes(A):
    l = A.bit_length()
    byte = l/8 + (0 if(l%8 == 0) else 1)
    return byte

ZOxLength = getNumOfBytes(Z)
print (ZOxLength)

