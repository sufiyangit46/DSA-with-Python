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


