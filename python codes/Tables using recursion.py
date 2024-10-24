#print table of a number with thr help of recursion
def fun(n,i):
    if i==11:
        return
    print(n*i)
    fun(n,i+1)
n=int(input())
fun(n,1)