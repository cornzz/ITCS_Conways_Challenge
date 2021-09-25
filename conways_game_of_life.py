def c(p,r):
	A=range;from itertools import product as s;m=lambda t,v,k:k(t,key=lambda w:w[v])[v]
	for i in A(r+1):
		if not p:return[]
		a,b=m(p,0,min),m(p,1,min);p=[(x-a,y-b)for(x,y)in p]
		if i==r:break
		d,e=m(p,0,max),m(p,1,max);p=[(x,y)for x in A(-1,d+2)for y in A(-1,e+2)if (8+16*((x,y)in p)>>sum((x+g,y+h)in p for(g,h)in s([-1,0,1],repeat=2)))&1]
	return p