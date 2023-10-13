a=input()
b=input()
m=[]
c=''
d=''
l=''
count=0
for i in range(max(len(a),len(b))):
    c+=a[i]
    for j in range(min(len(a),len(b))):
        d+=b[j]
        l+=" "+c+d
        # if c in d or d in c:
        #     count+=1
        # m[i][j]=count
print(l)
