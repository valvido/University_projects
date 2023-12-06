f1=open("acids.txt", "r")
ak=f1.readline()
f1.close()

print(ak)

bm=[] 
f1=open("blosum50.txt", "r")
for i in range(20):
    line=f1.readline()
    vc=line.split()
    bm.append(vc[:])
for i in range(20):
    for j in range(20):
        bm[i][j]=int(bm[i][j])

for i in range(20):
    print(bm[i])

x='HPEW'
y='PW'
m=len(x)
n=len(y)

sm=[]
tmp=[]
for i in range(m+1):
    tmp.append(0)
for i in range(n+1):
    sm.append(tmp[:])

for i in range (n+1):
    print(sm[i])
print("\n")
print(tmp)
print("\n")


for i in range(n+1):
    sm[i][0]=-8*i
for i in range(m+1):
    sm[0][i]=-8*i

for i in range (n+1):
    print(sm[i])
print("\n")


for i in range(1,n+1):
    for j in range(1,m+1):
        tmp=[]
        tmp.append(sm[i-1][j]-8)
        tmp.append(sm[i][j-1]-8)
        bb=bm[ak.index(y[i-1])][ak.index(x[j-1])]
        tmp.append(sm[i-1][j-1]+bb)
        tmp.sort()
        sm[i][j]=tmp[2]
        print('{0},{1}\n'.format(y[i-1],x[j-1]))
        print('{0},{1}\n'.format(ak.index(y[i-1]),ak.index(x[j-1])))

for i in range (n+1):
    print(sm[i])

print('\n')
	
rj = ''
s = ''

def traceback(s, i, j):

	if(i==0 and j==0):
		global rj 
		rj = rj + s + '\n'
		return

	if((i-1) > -1 and (sm[i-1][j]-8) == sm[i][j] ):
		s = 'G' + s
		traceback(s,i-1,j)
		
	if((j-1) > -1 and (sm[i][j-1]-8) == sm[i][j] ):
		s = 'L' + s
		traceback(s,i,j-1)
		
	bb=bm[ak.index(y[i-1])][ak.index(x[j-1])]	
	if((i-1) > -1 and (j-1) > -1 and(sm[i-1][j-1] + bb) == sm[i][j] ):
		s = 'D' + s
		traceback(s,i-1,j-1)
		
traceback(s, n, m)

print(rj)

k = len(rj.split('\n')[0])

q=0
w=0
kon1=''
kon2=''

for i in range(k):
	if(rj[i] == 'L'):
		kon1 = kon1 + x[q]
		kon2 = kon2 + '_'
		q=q+1
	else: 
		if(rj[i] == 'G'):
			kon1 = kon1 + '_'
			kon2 = kon2 + y[w]
			w=w+1
		else:
			kon1 = kon1 + x[q]
			kon2 = kon2 + y[w]
			q=q+1
			w=w+1
			
print(kon1)
print(kon2)
