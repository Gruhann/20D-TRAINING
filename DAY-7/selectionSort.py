l=[int(x) for x in input().split()]
n=len(l)
for i in range(n-1):
    mini=i
    for j in range(i+1,n):
        if l[j]<l[mini]:
            mini=j
    l[i],l[mini]=l[mini],l[i]
print(l)
