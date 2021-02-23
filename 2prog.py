def fact(n):
	if n==0:
		return 1
	else:
	   return n*fact(n-1)


x=int(input("enter the number "))
c=fact(x)
print("the factorial of the number is")
print(c)	   	