class A:
    def __init__(self, a):
        self.a=a
    def func(self):
        print(self.a)
class B:
    def __init__(self,a):
        self.a=a
    def func(self):
        print("b")
b=A(3)
b.func()
b=B(2)
b.func()