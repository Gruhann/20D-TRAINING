n=[x for x in input().split()]
c=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
                   if n[i]>n[j]:
                        c+=1
print(c)
