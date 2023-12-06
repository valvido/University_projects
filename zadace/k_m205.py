import random
import math
def sed(x,y): # square of euclidean distance
	dist=0
	for i in range(len(x)):
		dist = dist + (x[i]-y[i])*(x[i]-y[i])
	return dist
def sad(x,y): # simple addition of vectors
        v=[]
        for i in range(len(x)):
                v.append(x[i]+y[i])
        return v
f1=open("data01.txt", "r")
f2=open("res204.txt", "w")
noc=int(f1.readline()) # broj centara
nopt=int(f1.readline()) # broj tocaka
dimpt=int(f1.readline()) # dimenzija tocaka
noi=15 # broj iteracija
x=[]
for i in range(nopt):
	line=f1.readline() # citam jedan redak iz datoteke
	vector=line.split() # splittam redak u listu
	x.append(vector) # appendam listu u matricu
for i in range(nopt):
        for j in range(dimpt):
                x[i][j]=float(x[i][j])
cent=[]
for i in range(noc): # biramo potrebni broj slucajnih centara
        j=random.randint(0, nopt-1)
        cent.append(x[j][:])
gid=[]
for i in range(nopt): # punim listu gid (=group indicator), da bih je poslije mogao samo mijenjati
        gid.append(0)


# main loop, repeated "noi" times
for temp in range(10,1,-1):
        # odredjivanje clustera
        for i in range(nopt):
                c=sed(x[i],cent[0])
                suma=tmp_dist=c
                gid[i]=0
                for j in range(1,noc):
                        c=sed(x[i],cent[j])
                        suma=suma+c
                        if c < tmp_dist:
                                gid[i]=j
                                tmp_dist=c
                  
        # kraj odredjivanja clustera
        # odredjivanje novih centara
        for i in range(noc):
                v=[]
                for j in range(dimpt):
                        v.append(0)
                cl_count=0
                for j in range(nopt):
                        if gid[j]==i:
                                cl_count=cl_count+1
                                v=sad(v,x[j])
                if cl_count>0:
                        for j in range(dimpt):
                                cent[i][j]=v[j]*1.0/cl_count
        # kraj odredjivanja novih centara
        # ispis u file
        obj=0
        for i in range(nopt):
                obj=obj+sed(x[i],cent[gid[i]])        
        f2.write(' %s %3d %20.10f \n' % ('iteration', temp,obj))
f1.close()
f2.close()
