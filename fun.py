print("welcome")
def add(a,b=0,c=0,d=0,e=0):
    """
    a: int,float is mandatory
    b,c,d,e: int/float are optional
    syntax:add(a,[b,c,d,e])
    ex1: add(10,20)
    print the summation of the given values
    """
    print("a=%s,b=%s,c=%s,d=%s,e=%s"%(a,b,c,d,e))
    res=a+b+c+d+e
    print("result:",res)
add(c=10,d=200)
print("thank you!!")