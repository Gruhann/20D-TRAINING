# smallest number greater than n with exaxtly 1 bit diff in binary form 
# x=bin(15)
# x=str(x)
# x=x[2:]
# print(int(x))
n=int(input())
print(n|n+1)


