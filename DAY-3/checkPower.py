# check power of 2 or not
# check power of 4 or not

# n=int(input())
# for i in range(0,n):
#     if 2**i==n:
#         print("2 power",i)

# using bitwise


n=int(input())
count=0
while(n):
    count+=1
    n=n&(n-2)
if count==1:
    print("true")
else:
    print("false")
