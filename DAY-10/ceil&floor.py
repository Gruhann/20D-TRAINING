def floorr(n,target,start,last):
    if target<n[start]:
        return 0
    elif n[len(n)-1]<target:
        return n[len(n)-1]
    mid=(start+last)//2
    if n[mid]==target:
        return n[mid]
    elif n[mid]<target:
        if n[mid+1]>target:
            return n[mid]
        return floorr(n,target,start,mid-1)
    else:
        return floorr(n,target,mid-1,last)

def linearSearch_floor(n,target):
    for i in range(len(n)):
        if n[i]==target:
            return n[i]
        elif n[i]<target:
            if n[i+1]>target:
                return n[i]

def ceil(n,target,start,last):
    if target<n[start]:
        return n[start]
    elif n[len(n)-1]<target:
        return 0
    mid=(start+last)//2
    if n[mid]==target:
        return n[mid]
    elif n[mid]<target:
        
        return ceil(n,target,start,mid-1)
    else:
        if n[mid-1]<target:
            return n[mid]
        return ceil(n,target,mid-1,last)

def linearSearch_ceil(n,target):
    for i in range(len(n)):
        if n[i]==target:
            return n[i]
        elif n[i]>target:
            if n[i-1]<target:
                return n[i]

n=list(map(int,input().split()))
n.sort()
target=int(input())
start=0
last=len(n)-1
print('floor: ',floorr(n,target,start,last))
print(linearSearch_floor(n,target))
print("ceil: ",ceil(n,target,start,last))
print(linearSearch_ceil(n,target))