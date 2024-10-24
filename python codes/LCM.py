a=int(input())
b=int(input())
c=int(input())
m=max(a,b,c)
for i in range(m,(a*b*c)+1):
    if i%a==0 and i%b==0 and i%c==0:
        print("The answer is",i)
        break
    