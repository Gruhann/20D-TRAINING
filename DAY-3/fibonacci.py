#fibonacci using iteration
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        a=0 
        b =1
        for i in range(2, n + 1):
            c = a + b
            a,b = b,c
        return c

n=int(input())
for i in range(n):
    print(fib(i),end=" ")


# # fibonacci using recusion
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# n=int(input())
# for i in range(n):
#     print(fib(i),end=" ")


