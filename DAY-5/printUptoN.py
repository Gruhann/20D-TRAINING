#1 to n
# def p(n):
#     if n==0:
#         return 
#     p(n-1)
#     print(n,end=' ')
# n=int(input())
# p(n)

#n to 1
def p(n):
    if n==0:
        return 
    print(n,end=' ')
    p(n-1)  
n=int(input())
p(n)