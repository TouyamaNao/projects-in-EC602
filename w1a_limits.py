# calculate and print a table for the cap of integers using 1,2,4 and 8 bytes of# storage.
#


T = "{:<6}{:<22}{:<22}{:<22}"
print(T.format('Bytes', 'Largest Unsigned Int', 
		'Minimun Signed Int', 'Maximum Signed Int'))
testArray = [1,2,4,8];
for i in testArray:
    lui = 2**(i*8)-1
    minsi = -2**(i*8-1)
    maxsi = 2**(i*8-1)-1
    print(T.format(i, lui, minsi, maxsi))
