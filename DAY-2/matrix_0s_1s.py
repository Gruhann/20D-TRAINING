import random
a=[]
vertical_count_1=0
hor_count_1=0
ldiag_count_1=0
rdiag_count_1=0

vertical_count_0=0
hor_count_0=0
ldiag_count_0=0
rdiag_count_0=0

def check(a):
    print("hi")    

for i in range(0,4):
    b=[]
    for j in range(0,4):
        b.append(random.randint(0,1))
    a.append(b)
check(a)
print(a)
print("hor count 0 :",hor_count_0)
print("hor count 1 :",hor_count_1)
