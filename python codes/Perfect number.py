n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
if(sum(l)==n):
    print("perfect number")
else:
    print("not a perfect number")
