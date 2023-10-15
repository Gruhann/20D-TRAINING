n=int(input())
l=[True for x in range(n+1)]
p=2
while(p*p<n):
    if l[p]:
        for i in range(p*p,n+1,p):
            l[i]=False
    p+=1
for p in range(2,n+1):
    if l[p]:
        print(p,end=' ')