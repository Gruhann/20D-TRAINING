str1=input()

a=[ ]
b=list(str1)
s=""
rev=list(str1)
for i in range(len(str1)):
    if str1[i]==' ' or str1[i] in "[#!$%&'()*+-.,/:;<=>?@[\]^_`{|}~]":
        a.append(i)
    else:
        s+=str1[i]
rev=s[::-1]
print(rev)
prev=0
l=""
for i in a:
    for j in range(prev,i):
        if j < len(rev):
            l+=rev[j]
    l+=str1[i]
    prev=i  
print(l)
