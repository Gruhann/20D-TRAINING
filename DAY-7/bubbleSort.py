a=[int(x) for x in input().split()]
n=len(a)
flag=True
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            flag=False
            a[j],a[j+1]=a[j+1],a[j]
    if flag:
        break
print(a)
# ? total number of swaps and comparisions in worst case scenario is n*(n-1)/2
# first iteration n+1
# second iteration n+2
# .
# .
# .