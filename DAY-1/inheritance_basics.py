class Siva:
    def gold(warangal):
        print("price : 5L")
    def car(warangal):
        print("price : 6L")

class A(Siva):
    def bank(warangal):
        print("deposited 10L")

class gbaby(A):#child of A(no need to create object for A, can access from gbaby)
    def bat(warangal):
        print("bat is not available")

class B(Siva):
    def jewels(warangal):
        print("jewels buyed")



a=gbaby()
a.bat()
a.gold()
a.car()
a.bank()
# a.jewels()//can't perform this action coz both are childs 
# and we cant access one child function from other child variable

b=B()
b.gold()
b.car()
# b.bank()
b.jewels()