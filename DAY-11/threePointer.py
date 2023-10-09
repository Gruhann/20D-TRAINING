def find(n,target):
    for i in range(len(n)):
        a=n[i]
        if a==target:
            return a
        diff=target-a
        b=i+1
        c=len(n)-1
        while b<c:
            if n[b]+n[c]<diff:
                b+=1
            elif n[b]+n[c]>diff:
                c-=1
            else:
                return a,n[b],n[c]

    else:
        return "no subset of sum found"


n=list(map(int,input().split()))
target=int(input())
print(find(n,target))