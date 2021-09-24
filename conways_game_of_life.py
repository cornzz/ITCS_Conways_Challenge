def c(p,r):
	A=range;from itertools import product as D;B=lambda t,v:min(t,key=lambda w:w[v])[v];C=lambda t,v:max(p,key=lambda t:t[v])[v]
	for E in A(r+1):
		if not p:return[]
		F,G=B(p,0),B(p,1);p=[(A-F,B-G)for(A,B)in p]
		if E==r:break
		H,I=C(p,0),C(p,1);p=[(B,C)for B in A(-1,H+2)for C in A(-1,I+2)if 8+16*((B,C)in p)>>sum(((B+A,C+E)in p for(A,E)in D([-1,0,1],repeat=2)))&1]
	return p