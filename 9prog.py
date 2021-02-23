a=[]
while True:
	print("enter q to exit else enter the string")
	l=input()
	if l=='q':
		break
		
	else:
		a.append(l.upper())


for i in a:
	print(i)
