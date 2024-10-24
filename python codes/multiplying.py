n=int(input())
sum=1
while(n!=0):
  rem=n%10
  sum=sum*rem
  n=n//10
print(sum)