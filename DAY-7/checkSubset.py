def checkSubset(n, target):
    if target<0:
        return False,[]
    
    def backtrack(start,sum1,s):
        if sum1==target:
            return True, s[:]
        
        if sum1>target or start==len(n):
            return False,[]
        a, b = backtrack(start+1,sum1+n[start],s+[n[start]])
        if a:
            return True, b
        return backtrack(start + 1, sum1,s)
    return backtrack(0, 0, [])
n = list(map(int, input().split()))
target = int(input())
b, s = checkSubset(n, target)
if b:
    print(s)
else:
    print("No subset found.")
