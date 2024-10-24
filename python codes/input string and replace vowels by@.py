#Take input string and replace vowels by @ and space by _
s=input()
temp=""
for i in s:
    if i in "aeiouAEIOU":
        temp=temp+'@'
    elif i==" ":
        temp=temp+'_'
    else:
        temp=temp+i
print(temp)
