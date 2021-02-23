import math
l=[]
a=[]
v=input("enter the comma seperated values")
l=v.split(',')
def Q(i):
	return (str(round(math.sqrt(((2*50*int(i))/30)))))
	 
a=list(map(Q,l))
  
print( ','.join(a))