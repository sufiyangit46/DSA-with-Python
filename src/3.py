#26
# Max Consecutive Ones               # Optimal Method

nums=[1,0,1,0,0,1,0,1,1,1,1,0,1,0,1]
count=0
max_count=0
for i in range(0,len(nums)):
    if nums[i]==1:
        count+=1
    else:
        max_count=max(max_count,count)
        count=0
print(max_count)                     # TC O(N) AND SC O(1)

#27
# Two Sum Problem             # Brute Method

nums=[2,5,2,6,9,4,5,2]
target=13
n=len(nums)
for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            print([i,j])              # TC O(N2) AND SC O(1)

# Optimal Method

nums=[2,5,2,6,9,4,5,2]
n=len(nums)
hashmap={}
target=13
for i in range(0,n):
    remaining=target-nums[i]
    if remaining in hashmap:
        print([hashmap[remaining],i])
    else:
        hashmap[nums[i]]=i              # TC O(N) AND SC O(N)