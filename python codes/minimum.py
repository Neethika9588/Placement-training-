l=list(map(int,input().split()))
print(l)
max=l[0]
for i in l:
    if i<max:
        max=i
print(max)