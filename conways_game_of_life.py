from itertools import product as s
def c(p,r):
	m=lambda t,v:min(t,key=lambda w:w[v])[v]
	n=lambda t,v:max(p,key=lambda t:t[v])[v]
	for i in range(r+1):
		if not p:return[]
		d,e=m(p,0),m(p,1)
		p=[(x-d,y-e) for (x, y) in p]
		if i==r:break
		a=n(p,0)
		b=n(p,1)
		p_=[]
		for y in range(-1,b+2):
			for x in range(-1,a+2):
				if (8+16*((x,y)in p)>>sum((x+x_,y+y_)in p for(x_, y_)in s([-1,0,1],repeat=2)))&1:
					p_.append((x,y))
		p=p_
	return p