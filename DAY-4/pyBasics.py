
# print(chr(65))#to print the character from ascii 
# print(ord('/'))#to print ascii value of a character

# a="helloh"
# print(a.index("h"))#to find index of the specified character
# print(a.rindex("h"))#to find index of the last occurance of the specified character

#to print the character after specified jump number
# a=input()
# b=int(input())
# x=ord(a)+b
# if x>122:
#     x=x-26
# print(chr(x))

#pattern 1
#n=int(input())
# for i in range(n):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#using single for loop
# for i in range(n):
#     print("* "*(i+1))

#triangle equilateral
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#using one for loop
# for i in range(n):
#     print(" "*(n-i)+"* "*(i))

#inverted triangle
# for i in range(n):
#     print(" "*(i)+ "* "*(n-i))

#diamond
# for i in range(n):
#     print(" "*(n-i)+"* "*(i))
# for i in range(n):
#     print(" "*(i)+ "* "*(n-i))

#pattern 2
# n=int(input())
# for i in range(n):
#     print(str(i+1) *(i+1))

# n=int(input())
# for i in range(1,n+1):
#     print((10**(i)//9)*i)


##############################  FUNCTIONS #################################

def cse():
    print("cse")
def ece(*x):
    print("ece",x)
ece(1,2)
cse()