#2
# % give the last digit of a number and // remove the last digit.

#basic operation and fundamental

n=45687
last=n%10
print(last)
remove=n//10
print(remove)

#3
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

#To check palindrome

a=int(input())
num=a
result=0
while num>0:
    ld=num%10
    result=result*10+ld
    num=num//10
if result==a:
    print("Palindrome")
else:
    print("Not Palindrome")

#To check armstrong number

a=int(input())
num=a
nod=len(str(num))
result=0
while num>0:
    ld=num%10
    result=result+ld**nod
    num=num//10
if result==a:
    print("Armstrong")
else:
    print("Not Armstrong")

#







