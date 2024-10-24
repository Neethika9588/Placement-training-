#counting the number of elements in a list
l=[1,1,2,2,2,3,3,3,3]
temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
for i in temp:
    c=0
    for j in l:
        if i==j:
          c+=1
    print(i,"-",c)
        