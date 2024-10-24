#the numbers in a stack are in reverse order.
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
    print(n)
fun(3)