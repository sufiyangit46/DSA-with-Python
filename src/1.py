# % give the last digit of a number and // remove the last digit.

#basic operation and fundamental

n=45687
last=n%10
print(last)
remove=n//10
print(remove)


#count the number of digit

n=8754685
count=0
while n>0:
    n=n//10
    count+=1
print(count)

# to count number of digit we can use log base 10 and add 1 and then convert to integer

from math import *
n=5468
def digit(n):
    return int(log10(n))+1
print(digit(n))







