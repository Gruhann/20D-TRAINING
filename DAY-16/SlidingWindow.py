n=list(map(int,input().split()))
target=int(input())
# i=0
# j=1
# currSum=n[0]
# while j<len(n):
    
#     if n[i]+n[j]==target:
#         print(n[i],n[j])
#         break
#     i+=1
#     j+=1
i=0
j=0
currSum=n[0]
while j<len(n)-1:
    if currSum==target:
        print("sum from index",i,"to",j,"is",currSum)
        break
    elif currSum>target:
        currSum-=n[i]
        i=i+1
    else:
        j=j+1
        currSum+=n[j]
