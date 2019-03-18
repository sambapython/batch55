from mod1 import c1
class own_c1(c1):
	def fun1(self):
		c1.fun1(self)
		print("some extra code in fun1 of c1")
	def fun2(self):
		print("this is fun2") 
o1=own_c1()
o1.fun1()
o1.fun2()