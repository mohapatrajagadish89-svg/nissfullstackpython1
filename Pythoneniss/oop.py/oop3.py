class simple:
	def __init__(self,p,r,t):
	   self.p=p
	   self.rate=r
	   self.time=t
	def show(self):
	    print("principle=",self.p)
	    print("rate=",self.rate) 
	    print("time=",self.time)
	def sical(self):
		return self.p*self.rate*self.time/100
print("enter principle rate and time")
pr=float(input())
r=float(input())
t=float(input())		   
i1=simple(pr,r,t)
i1.show()
print("simple intrest=",i1.sical())    


