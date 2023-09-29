# find missing num using binary ops(xor)
 
x=[0,1,3,4,5,6,7,8,9,10,11]
n = len(x)
a=0
b=0
for i in range(len(x)+1):
    a=a^i
for i in x:
    b=b^i
c=a^b
print(c)

# //missing number in array
# int a[]={1,2,3,4,6,7};
# int x=0,i=0;
# for(i=0;i<=6;i++)
# x=x^i;
# for(i=0;i<6-1;i++)
# x=x^a[i];
# printf("%d",x);	
# }