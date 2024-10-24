#print vowels from a Strings
a=input()
temp=" "
for i in a:
   if i in "aeiouAEIOU":
    temp=temp+i
print(temp)