#Anagram-same letters with different meaning 
s=input()
s1=input()
if len(s)!=len(s1):
    print("not anagram")
else:
    for i in s:
        if s.count(i)!=s1.count(i):
            print("not anagram")
            break
    print("anagram")
