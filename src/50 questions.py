# 1 REVERSE A STRING

num='pipeline'
char=list(num)
n=len(char)
i=0
j=n-1
while i<j:
    char[i],char[j]=char[j],char[i]
    i+=1
    j-=1
print(''.join(char))

# TC O(N) AND SC O(1) BUT IN PYTHON SC O(N) BECAUSE WE CONVERT TO LIST
# TWO POINTER TECHNIQUE IS THE APPROACH TO SOLVE THIS QUESTION


# 2 CHECK WHETHER A STRING IS A PALINDROME

num=(input())
a=num
n=len(a)
i=0
j=n-1
while i<j:
    if a[i]!=a[j]:
        print("Not Palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")

# TC O(N) AND SC O(1)
# TWO POINTER TECHNIQUE IS THE APPROACH TO CHECK WHETHER IT IS PALINDROME OR NOT


# 3 FIND THE FIRST NON-REPEATING CHARACTER

ch='shaikh'
n=len(ch)
di={}
for i in ch:
    if i not in di:
        di[i]=1
    else:
        di[i]+=1
for j in ch:
    if di[j]==1:
        print(j)
        break

# TC O(N) AND SC O(N)
# WE USE HASH MAP(DICTIONARY) TO STORE FREQUENCY AND THEN LOOP ON ORIGINAL STRING TO CHECK THE FIRST NON-REPEATING CHARACTER


# 4 CHECK WHETHER TWO STRINGS ARE ANAGRAMS

ch1='listen'
ch2='silent'
di={}
if len(ch1)!=len(ch2):
    print("Not Anagram")
    exit()
for i in ch1:
    if i not in di:
        di[i]=1
    else:
        di[i]+=1
for i in ch2:
    if i not in di:
        print("Not Anagram")
        break
    di[i]-=1
for v in di.values():
    if v!=0:
        print("Not Anagram")
        break
else:
    print("Anagram")

# TC O(N) AND SC O(N)
# ANAGRAM STRING ARE THOSE WHOSE CHARACTER AND THEIR LENGTH IS SAME AND ORDER IS NOT NECESSARY SO WE SOLVE THIS USING HASH MAP(DICTIONARY)
# FIRST WE STORE ALL CHARACTER IN DICTIONARY AND THEN CHECK THE 2 STRING CHARACTER ARE PRESENT OR NOT THEN WE SUBTRACT THE COUNT OF CHARACTER
# SO IF THE VALUE IN DICTIONARY IS 0 THEN IT IS ANAGRAM IF NOT THEN IT IS NOT ANAGRAM


# 5 FIND THE MOST FREQUENT CHARACTER

ch='banana'
di={}
for i in ch:
    if i not in di:
        di[i]=1
    else:
        di[i]+=1
m=0
fr=''
for key,value in di.items():
    if value>m:
        m=value
        fr=key
print(fr)

# TC O(N) AND SC O(N)
# WE SOLVE THIS USING HASH MAP TO STORE CHARACTER AND THEN RUN A LOOP TO GET THE HIGHEST FREQUENCY CHARACTER AND PRINT THE CHARACTER
