#11
# Find the Fibonacci number using Recursion

a=int(input())
def fibo(a):
    if a==0 or a==1:
        return a
    return fibo(a-1)+fibo(a-2)
print(fibo(a))

# Using While loop

s=int(input())
count=0
a,b=0,1
while count<s:
    print(a,end=" ")
    a,b=b,a+b
    count+=1
print(a)

# Using For loop

s=int(input())
a,b=0,1
for i in range(s):
    print(a,end=" ")
    a,b=b,a+b
print(a)

# Selection Sort
