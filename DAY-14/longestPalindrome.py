a=input()
left=0
right=len(a)-1
l=[]
p=[]
la=0
for i in range(len(a)):
    c=""
    for j in range(left,len(a)):
        c+=a[j]
        if c not in l:
            l.append(c)
    left+=1
for i in l:
    if i==i[::-1]:
        if i not in p:
            if len(i)>la:
                la=len(i)
            p.append(i)
for i in p:
    if len(i)==la:
        print(i)