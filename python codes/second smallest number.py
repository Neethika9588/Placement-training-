l=list(map(int,input().split()))
m=min(l)
second=m
for i in l:
    if i<m:
        second=m
        m=i
print(second)    