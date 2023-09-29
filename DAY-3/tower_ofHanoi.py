def toh(n,source,auxilary,destination):
    if n==0:
        return n
    toh(n-1,source,destination,auxilary)
    print("disk",n,"moved from",source,"to",destination)
    toh(n-1,auxilary,source,destination)
n=int(input())
source,auxilary,destination=input().split()
toh(n,source,auxilary,destination)