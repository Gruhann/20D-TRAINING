class Siva:
    def __init__(mango,mango1=None):
        print("mango construtor")#constructer will be automatically 
                                 #called implicitly by the interpretor in python
    def __init__(self,mango2):
        print("2 parameter constructor",mango2)
    def __bank__(india):
        print("Test1")
    def A(abc):
        print("Test2")
    def B(abc):
        print("Test3")


s=Siva(225)
s.A()
s.B()
s.__bank__()
#passing arg for mango2