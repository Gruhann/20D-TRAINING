
def sqrt(n,start,last):
    if n<=0:
        return "not positive"
    elif n==1:
        return 1
    mid=(start+last)//2
    if mid*mid==n:
        return mid
    elif mid*mid<n:
        if (mid+1)*(mid+1)>n:
            return n/mid
        return sqrt(n,mid+1,last)
    else:
        return sqrt(n,start,mid-1)   

n=int(input())
print(sqrt(n,0,n//2))
