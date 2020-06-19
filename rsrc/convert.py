from panda3d.core import LPoint3d, Triangulator3
import glob
import os
import re
import shutil



ROUND_DIGITS=5



for fp in glob.glob("*.obj",recursive=True):
	if (fp[0]=="2"):
		continue
	def _round(x):
		return round(x*10**ROUND_DIGITS)/10**ROUND_DIGITS
	with open(fp,"r") as f:
		sdt=f.read().split("\n")
		dt=[]
		vl=[]
		mn=None
		for k in sdt:
			k=k.strip()
			if (k.startswith("v ")):
				vl+=[[float(x) for x in k.split(" ")[1:] if x!=""]]
				mn=(vl[-1] if mn==None else [min(mn[_],vl[-1][_]) for _ in range(0,3)])
			elif (k.startswith("f")):
				tc=Triangulator3()
				l=0
				ol=[]
				for e in k.split(" ")[1:]:
					if (e.split("/")[0]==""):
						continue
					ol+=[[int(e.split("/")[0]),e]]
					tc.addPolygonVertex(tc.addVertex(*vl[int(e.split("/")[0])-1]))
					l+=1
				if (l==3):
					dt+=["f "+str(ol[0][1])+" "+str(ol[1][1])+" "+str(ol[2][1])]
				else:
					tc.triangulate()
					for l in range(0,tc.getNumTriangles()):
						dt+=[f"f {ol[tc.getTriangleV0(l)][1]} {ol[tc.getTriangleV1(l)][1]} {ol[tc.getTriangleV2(l)][1]}"]
			else:
				dt+=[k]
		mx=None
		mxl=[None,None,None]
		for v in vl:
			for _ in range(0,3):
				if (mx==None):
					mx=v[_]-mn[_]
				else:
					mx=max(mx,v[_]-mn[_])
				if (_==1):
					continue
				if (mxl[_]==None):
					mxl[_]=v[_]-mn[_]
				else:
					mxl[_]=max(mxl[_],v[_]-mn[_])
		mxl[1]=mx
		off=[(1-mxl[_]/mx)/2 for _ in range(0,3)]
		dt=[dt[0]]+["v "+" ".join([str(_round((v[_]-mn[_])/mx+off[_])) for _ in range(0,3)]) for v in vl]+dt[1:]
	with open(f"2{fp}","w") as f:
		f.write("\n".join(dt))
