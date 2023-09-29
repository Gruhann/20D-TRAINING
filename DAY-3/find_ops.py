n=int(input())
count=0
while(n):
    count+=1 #to count the number of digits in the binary code of the given input
    n=n&(n-1)
print("count of set bits : ",count)
