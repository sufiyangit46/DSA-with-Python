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
print(insertion(nums))

#12
# Merge two sorted array
# Merge Array

left=[1,2,3,4]
right=[1,1,3,4,5,6,7]
def merge_array(left,right):
    result=[]
    i,j=0,0
    n,m=len(left),len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result
print(merge_array(left,right))

# Merge Sort

nums=[3,1,2,4,1,5,2,6,4]
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left_arr=nums[:mid]
    right_arr=nums[mid:]
    left=merge_sort(left_arr)
    right=merge_sort(right_arr)
    return merge_array(left,right)
print(merge_sort(nums))

#13
# Revision of Selection, Bubble, Insertion and Merge Sort

#14
# All Revision and till exam end all topic revision and after exam continue from V......  from 15
# M 1

#15  M 15
# Quick Sort

nums=[5,1,8,2,4,7,9,3]
def partition(nums,low,high):
    pivot=nums[low]
    i=low
    j=high
    while i<j:
        while nums[i]<=pivot and i<high:
            i+=1
        while nums[j]>=pivot and j>low:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low],nums[j]=nums[j],nums[low]
    return j
def quick(nums,low,high):
    if low<high:
        ind=partition(nums,low,high)
        quick(nums,low,ind-1)
        quick(nums,ind+1,high)
quick(nums,0,len(nums)-1)
print(nums)

# LeetCode Questions
# Only Optimal solution
#16
# Find the largest element in an array

nums=[55,32,-97,99,3,67]
largest=nums[0]
n=len(nums)
for i in range(0,n):
    if nums[i]>largest:
        largest=nums[i]
print(largest)                 # TC O(N)  AND SC O(1)

#17
# Find the 2nd largest element in an array without sorting

nums=[55,32,-97,99,3,67,23]
n=len(nums)
largest=nums[0]
se_largest=nums[0]
for i in range(n):
    if nums[i]>largest:
        se_largest=largest
        largest=nums[i]
    elif nums[i]>se_largest and nums[i]!=largest:
        se_largest=nums[i]
print(se_largest)                 # TC O(N)  AND SC O(1)

#18
# Check if an array is sorted

nums=[1,2,3,4,5,6,7,8]
def sort(nums):
    n=len(nums)
    for i in range(1,n-1):
        if nums[i]>nums[i+1]:
            return False
    return True
print(sort(nums))                # TC O(N) AND SC O(1)

#19
# Remove duplicates from a sorted array      # Brute force code

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
freq={}
n=len(nums)
for i in range(0,n):
    freq[nums[i]]=0
j=0
for m in freq:
    freq[m]=nums[j]
    j+=1
print(j)                      # TC O(N) AND SC O(N)

# Optimal Two Pointer Approach

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
i=0
j=1
n=len(nums)
if nums==1:
    print(1)
while j<n:
    if nums[j]!=nums[i]:
        i+=1
        nums[j],nums[i]=nums[i],nums[j]
    j+=1
print(i+1)                    # TC O(N) AND SC O(1)

#20
# Right Rotate an Array by 1 Place            # By Slicing

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
n=len(nums)
nums[:]=[nums[n-1]]+nums[0:n-1]             # Can't concat int and list so we make int list by adding []
print(nums)                          # TC O(N) AND SC O(1) because we use [:] to perform inplace

# By Using loop

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
n=len(nums)
temp=nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]
nums[0]=temp
print(nums)                      # TC O(N) AND SC O(1)

#21
# Right Rotate an Array by k Place
# Brute Force Code

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
k=4
n=len(nums)
r=k%n
for _ in range(0,r):
    e=nums.pop()
    nums.insert(0,e)
print(nums)                    # TC O(r*n) AND SC O(1)

# Better Solution

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
k=4
n=len(nums)
k=k%n
nums[:]=nums[n-k:]+nums[:n-k]
print(nums)                    # TC O(N) AND SC O(1)

# Optimal Solution (Three Reversals)

nums=[1,1,1,2,2,3,3,4,5,6,9,9,9,9,10]
n=len(nums)
k=5
def reverse(nums,l,r):
    if nums==1:
        return nums
    while l<r:
        nums[l],nums[r]=nums[r],nums[l]
        l+=1
        r-=1
    return nums
reverse(nums,n-k,n-1)        # Reverse last k element
reverse(nums,0,n-k-1)     # Reverse remaining elements
reverse(nums,0,n-1)       # Reverse whole array
print(nums)                 # TC O(N) AND SC O(1)

#22
# Move Zeros to the end of the List
# Brute Force Code

nums=[1,2,0,2,3,5,0,4,0,0,2,5]
n=len(nums)
temp=[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz=len(temp)
for i in range(0,nz):
    nums[i]=temp[i]
for i in range(nz,n):
    nums[i]=0
print(nums)                 # TC O(N) AND SC O(N)