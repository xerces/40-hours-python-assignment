v=input(enter comma seperated values)
v=v.split(',')
r=int(v[0])
c=int(v[1])
m=[[0 for c in range(c)] for r in range(r)]

for i in range(r):
	for j in range(c):
		m[i][j]=i*j
                  


print(m)		