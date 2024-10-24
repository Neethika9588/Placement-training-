#Abundant 
n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
if(sum(l)>n):
    print("Abundant number")
else:
    print(" Not a Abundant number")