class A:
    def someFunc(self):
        print("Some function under class A")


class B:
    pass


class C(B,A):
    pass


obj = C()
#obj.someFunc()
print(C.mro())
# output: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
