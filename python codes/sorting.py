#Take an integer list from the user and print sorted list after removing duplicates
l=list(map(int,input().split()))
l=sorted(set(l))# Sorted can be used only with list,tuple,set
print(l)
