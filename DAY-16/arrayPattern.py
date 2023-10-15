n=list(map(int,input().split()))
# for i in range(len(n)):
#     print("*"*n[i])
#print horizontally ^

#print vetically
m=max(n)
for i in range(m,0,-1):
    print(f"{i:2d} | ",end="") 
    for j in n:
        if j>=i:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()