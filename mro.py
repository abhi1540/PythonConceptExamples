class A(object):
    def dothis(self):
        print("doing this in A")


class B(A):
    pass


class C(object):
    def dothis(self):
        print("doing this for C")


class D(B,C):
    pass


d_instance = D()
d_instance.dothis()

print(D.mro())