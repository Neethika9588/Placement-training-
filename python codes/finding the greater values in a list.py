#finding the greater values in a given list of elements
l=list(map(int,input().split()))
result=[]
for i in range(len(l)):
    c=0
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            c+=1
    result.append(c)
print(result)
#output:1 2 3 2 3 4
#[5, 3, 1, 2, 1, 0]
