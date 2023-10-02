import random
def island(a,i,j,c):
    if a[i][j]==1:
        a[i][j] =0
    if a[i][j]==0:    
        return
    if i<n-1:
        island(a,i+1,j,c)
    if i>0:
        island(a,i-1,j,c)
    if j<n-1:
        island(a,i,j+1,c)
    if j>0:
        island(a,i,j-1,c)
    return c
n=int(input())
a=[]
for i in range(n):
    b=[]
    for j in range(n):
        b.append(random.randint(0,1))
    a.append(b)
print(a)
print(island(a,0,0,0))
