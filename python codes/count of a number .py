n=int(input())
a=1
count=0
while(n>0):
    rem=n%10
    if rem==a:
        count+=1
    n//=10
print(count)