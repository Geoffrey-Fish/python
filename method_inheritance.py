class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B Method")

class C(B):
    def third_method(self):
        print("C Method")

c = C()
c.method()
c.another_method()
c.third_method()