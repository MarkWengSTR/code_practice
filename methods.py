class A(object):
    bar = 42

    def foo(self):
        pass


class B(object):
    bar = 0


class C(A, B):
    xyz = 'abc'

    def foo(self):
        super().foo()


# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
print(C.mro())
print(C().foo)  # 42

print(super(B).__self__)  # None
print(super(B, B()).__self__)  # <__main__.B object at 0x000002780C2FF5B0>
