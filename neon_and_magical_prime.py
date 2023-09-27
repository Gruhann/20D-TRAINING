import math 
class Siva:
    def gold(warangal):
        print("price : 5L")
    def car(warangal):
        print("price : 6L")
        
class A(Siva):
    def magical_prime(warangal,p,q):
        for a in range(p + 1, q):
            flag = True
            for i in range(2, int(math.sqrt(a)) + 1):
                if a % i == 0:
                    flag = False
                    break
            if flag:
                reversed_a = int(str(a)[::-1])
            if reversed_a == a:
                print("Magical prime:", a)
                       
class B(Siva):
    def neon(warangal,p,q):
        for a in range(p+1,q):
            temp=a
            s=a*a
            sum=0
            while s!=0:
                rem=s%10
                sum+= rem
                s//= 10
            if sum==temp:
                 print("Neon number",temp)

c=A()
c.magical_prime(0,100)
b=B()
b.neon(0,100)
