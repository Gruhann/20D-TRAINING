# n=input()
# def pal(str):
#     j=len(str)
#     if j==1:
#         return True
#     for i in range(j//2):
#         if str[i]==str[j-i-1]:
#             return True
#         return False

# print(pal(n))

# n=input()
# rev=n[::-1]
# if rev==n:
#     print("palindrome")

#recursive palindrome
n=input()
def check(n,i,j):
    if n[i]!=n[j]:
        return False    
    if i>j:
        return True
    return check(n,i+1,j-1)

i=0
j=len(n)-1    
print(check(n,i,j))
        