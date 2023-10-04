n=int(input())
def toh(n,s,a,d):

    if n==1:
        return 1
    c1=toh(n-1,s,d,a)
    c2=1 
    c3=toh(n-1,a,s,d)
    return c1+c2+c3
    
print(toh(n,'A','B','C'))