# print lonely integers in an array using bitwise
a=[10,20,30,20,10]
# for i in a:
#     if a.count(i)==1:
#         print(i,end=" ")
res=0
for i in a:
    res=res^i
print(res)
