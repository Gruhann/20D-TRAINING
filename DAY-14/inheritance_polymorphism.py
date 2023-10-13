class cse:
    def __init__(self):
        print("Delault constructor")
    def fun1(self):
        print("fun1")
class aiml(cse):
    def fun2(self):
        print("AIML")
    def fun2(self):#polymorphism : updates the written function with same name
        print("fun2")
a=aiml()#inheritance: we can access th parent's function by creating an object for child class
a.fun1()
a.fun2()