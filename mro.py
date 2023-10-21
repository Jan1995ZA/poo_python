class A:
    def hablar(self):
        print("Hola A")

class B(A):
    def hablar(self):
        print("Hola B")

class C(A):
    def hablar(self):
        print("Hola C")

class D(B,C):
    def hablar(self):
        print("Hola D")

d = D()     
d.hablar()

print(D.mro())