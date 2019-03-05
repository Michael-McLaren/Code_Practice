a = [1,2,3,4,5,6,12,3,2312,41,35,12,42,4,2,4,2,4,2,5,1,2,4,5,56]
b = [2312,1,2,3,41,4,5,6,124,125,135,4,4,53,24,3,423,54,3,324]

def array_diff(a,b):
	c = a+b
	for  x in (a+b):
		if (a+b).count(x)!=1:
			c.remove(x)
	return c



print(array_diff(a,b))
