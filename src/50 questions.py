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


# 6 LONGEST COMMON PREFIX

str=['flow','flower','flight']
if not str:
    print('')
prefix=str[0]
for i in str[1:]:
    while not i.startswith(prefix):
        prefix=prefix[:-1]
print(prefix)

# TC O(N*M2) AND SC O(1)
# WE SOLVE THIS USING HORIZONTAL APPROACH FIRST WE TAKE FIRST STRING AND COMPARE REST OF THEM THAT STARTS WITH SAME CHARACTER AND KEEP SHRINKING


# 7 COMPRESS A STRING WITH COUNTS

ch='aaabbc'
result=''
count=1
for i in range(1,len(ch)):
    if ch[i]==ch[i-1]:
        count+=1
    else:
        result+=ch[i-1]+str(count)
        count=1
result+=ch[-1]+str(count)
print(result)

# TC O(N) AND SC O(N)
# WE SOLVE THIS USING COMPRESS THE STRING APPROACH WHERE INITIAL COUNT IS 1 AND EMPTY STRING TO STORE RESULT AND RUN A LOOP ON THE STRING
# IF PREVIOUS CH' IS SAME THEN COUNT+=1 IF NOT THEN WE ADD IT TO RESULT AND WE MANUALLY ADDED THE LAST CHARACTER BEACUSE THE LOOP END AT LAST CH'


# 8 VALIDATE PARENTHESES

st='({[]})'
def parent(st):
    pairs={')':'(','}':'{',']':'['}
    stack=[]
    for i in st:
        if i in '({[':
            stack.append(i)
        elif i in ')}]':
            if not stack or stack[-1]!=pairs[i]:
                return False
            stack.pop()
    return not stack
print(parent(st))

# TC O(N) AND SC O(N)
# WE SOLVED THIS USING A STACK TO STORE THE OPEN BRACKET AND CREATED PAIRS TO MATCH THE STACK TOP ELEMENT WITH PAIRS IF NOT MATCH RETURN FALSE
# THEN WE POP THE STACK TOP ELEMENT IF THE PAIR IS MATCHED AND LASTLY RETURN TRUE IF STACK IS EMPTY BECAUSE IF PAIR MATCHED NOTHING LEFT