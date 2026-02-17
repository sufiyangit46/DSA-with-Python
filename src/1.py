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

#4
# print all factors of a number

a=int(input())
i=1
result=[]
while i<=a:
    if a%i==0:
        result.append(i)
    i+=1
print(result)

# better solution use iteration till half of the input and append the input in last

a=int(input())
i=a//2
p=1
result=[]
while p<=i:
    if a%p==0:
        result.append(p)
    p+=1
result.append(a)
print(result)

# optimal solution for factor of number use sqrt function and output is not in sequence so we do sort

from math import sqrt
a=int(input())
i=1
p=sqrt(a)
result=[]
while i<=p:
    if a%i==0:
        result.append(i)
        if a//i!=i:
            result.append(a//i)
    i+=1
result.sort()
print(result)

# Store frequency of number in dictionary

list=[1,2,5,6,4,5,7,2,4]
dict={}
for i in range (1,len(list)):
    if list[i] in dict:
        dict[list[i]]+=1
    else:
        dict[list[i]]=1
print(dict)

# Method 2 using .get (hash map)

list=[1,2,3,4,5,1,2,3,4]
hash={}
for i in range(len(list)):
    hash[list[i]]=hash.get(list[i],0)+1
print(hash)

#5
# Hashing in Python # Brute method

n=[5,3,2,1,7,7,5,5,5,9,10]
m=[10,9,111,1,5,9,62]

for num in m:
    count=0
    for i in n:
        if i==num:
            count+=1
    print(count)

#Optimal method    #List

n=[5,3,2,1,7,7,5,5,5,9,10]
m=[10,9,111,1,5,9,62]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if num<1 or num>10:
        print(0)
    else:
        print(hash_list[num])

#6
# Hashing in Dictionary

n=[5,3,2,1,7,7,5,5,5,9,10]
m=[10,9,111,1,5,9,62]
dict={}
for i in n:
    dict[i]=dict.get(i,0)+1
for i in m:
    print(dict.get(i,0))

# Character Hashing  #Brute method

s='azyxyyzaaaa'
q='d','a','y','x'
for i in q:
    count=0
    for j in s:
        if j==i:
            count+=1
    print(count)

# Character Hashing  #Optimal method  using list, ascii and index

s='azyxyyzaaaa'
q='d','a','y','x'
list=[0]*27
for i in s:
    ascii=ord(i)
    index=ascii-97
    list[index]+=1
for i in q:
    ascii=ord(i)
    index=ascii-97
    print(list[index])

# Learned recursion (head and tail) and till V12 done and start 13
#Head Recursion using global variable

count=0
def func():
    global count
    if count==4:
        return
    count+=1
    func()
    print('Sufiyan')
func()

# Without global variable (optimal and safer in interview)

def func(count):
    if count==4:
        return
    func(count+1)
    print('Sufiyan')
func(0)

# Tail Recursion using global variable

count=0
def func():
    global count
    if count==4:
        return
    print('Sufiyan')
    count+=1
    func()
func()

# Without global variable  (optimal and safer in interview)

def func(count):
    if count==4:
        return
    print('Sufiyan')
    func(count+1)
func(0)

#7
# Recursion using Parameters
# Print 1 to N    (Tail Recursion)

def para(i,n):
    if i>n:
        return
    print(i)
    para(i+1,n)
para(1,4)

# Print N to 1

def para(n):
    if n==0:
        return
    print(n)
    para(n-1)
para(4)

# Print 1 to N     (Head Recursion)  (Backtracking)

def para(n):
    if n==0:
        return
    para(n-1)
    print(n)
para(4)

# Print N to 1

def para(i,n):
    if i>n:
        return
    para(i+1,n)
    print(i)
para(1,4)

#8
# Parameterized Recursion
# Sum of 1 to N   [Parameterized]

def para(sum,i,n):
    if i>n:
        print(sum)
        return
    para(sum+i,i+1,n)
para(0,1,10)

# Functional Recursion
# Sum of 1 to N   [Functional]

def para(n):
    if n==1:
        return 1
    return n+para(n-1)
print(para(4))

#9
# Factorial of a number

def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
print(fact(5))

#10
# Reverse an array using Recursion

arr=[1,2,3,4,5,6,7,8]
l=0
r=len(arr)-1
def reverse(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse(arr,l+1,r-1)
    return arr
print(reverse(arr,l,r))

# Using While loop

arr=[1,2,3,4,5,6,7,8]
l=0
r=len(arr)-1
def reverse(arr,l,r):
    while l<=r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
print(reverse(arr,l,r))

# Using For loop

arr=[1,2,3,4,5,6,7,8]
def reverse(arr):
    for i in range(len(arr)//2):
        r=len(arr)-1-i
        arr[i],arr[r]=arr[r],arr[i]
    return arr
print(reverse(arr))

# String is Palindrome or not using Recursion

a=(input())
l=0
r=len(a)-1
def palin(a,l,r):
    if l>=r:
        return True
    if a[l]!=a[r]:
        return False
    return palin(a,l+1,r-1)
print(palin(a,l,r))

# Using While loop

a=(input())
l=0
r=len(a)-1
def palin(a,l,r):
    while l<=r:
        if a[l]!=a[r]:
            return False
        l+=1
        r-=1
    return True
print(palin(a,l,r))



































































