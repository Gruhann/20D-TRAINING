def checkSubset(n, target):
    if target<0:
        return False,[]
    a=[]
    def backtrack(start,sum1,s):
        if sum1==target:
            a.append(s)
            return True, s[:]
        
        if sum1>target or start==len(n):
            return
        s.append(n[start]) 
        backtrack(start+1,sum1+n[start],s)
        s.pop()
        backtrack(start+1,sum1,s)
        return backtrack(start + 1, sum1,s)
    return backtrack(0, 0, [])
n = list(map(int, input().split()))
target = int(input())
checkSubset(n, target)
print(n)
