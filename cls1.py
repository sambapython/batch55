def fun():
    print("fun")
class cls:
    a=1000
    b=2000
    def fun1(x):
        print("x=",x)
        print("this is fun1 inside class")
print(cls.a,cls.b)
print(cls.fun1(200))