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

nums=[5,1,8,2,4,7,9,3]
def selection(nums):
    n=len(nums)
    for i in range(n):
        min_ind=i
        for j in range(i+1,n):
            if nums[j]<nums[min_ind]:
                min_ind=j
        nums[i],nums[min_ind]=nums[min_ind],nums[i]
    return nums
print(selection(nums))

# Bubble Sort

nums=[5,1,8,2,4,7,9,3]
def bubble(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
print(bubble(nums))

# Insertion Sort

nums=[5,1,8,2,4,7,9,3]
def insertion(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and nums[j]>key:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums



