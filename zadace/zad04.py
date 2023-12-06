f1=open("acids.txt", "r") ## citamo kiseline iz datoteke
ak=f1.readline()
f1.close()

bm=[] ## ucitavanje matrice
f1=open("blosum50.txt", "r")
for i in range(20):
    line=f1.readline()
    vc=line.split() 
    bm.append(vc[:])
for i in range(20): ## ucitavanje druge matrice
    for j in range(20):
        bm[i][j]=int(bm[i][j])
    
x='RALLWLAWWWWALAA' 
y='GLALWRWW' 
m=len(x)
n=len(y)

sm=[] ## matrica scorea
tmp=[]
for i in range(m+1):
    tmp.append(0) 
for i in range(n+1):
    sm.append(tmp[:]) 
for i in range(n+1):
    sm[i][0]=0
for i in range(m+1):
    sm[0][i]=0 
novi=[]
tmp=[]
## novi matrica sprema setnju
for i in range(m+1):
    tmp.append((0,0))
for i in range(n+1):
    novi.append(tmp[:]) ## rubni uvjeti
for i in range(1,n+1):
    novi[i][0]=((i-1),(0)) 
for j in range(1,m+1): 
    novi[0][j]=((0),(j-1))
## rekurzija- Smith-Watermantov algoritam
for i in range(1,n+1):
    for j in range(1,m+1): 
        tmp=[]
        tmp.append(sm[i-1][j]-8) 
        tmp.append(sm[i][j-1]-8) 
        tmp.append(0) 
        bb=bm[ak.index(y[i-1])][ak.index(x[j-1])] 
        tmp.append(sm[i-1][j-1]+bb)

 ## trazimo susjedne cvorove (i,j) 
naj=max(sm[i-1][j-1]+bb,sm[i][j-1]-8,sm[i-1][j]-8) 
if (naj==sm[i-1][j-1]+bb):
    novi[i][j]=((i-1),(j-1))
if (naj==sm[i-1][j]-8): 
    novi[i][j]=((i-1),(j))
if (naj==sm[i][j-1]-8): 
    novi[i][j]=((i),(j-1))
## kraj
tmp.sort() 
sm[i][j]=tmp[3]
## konstruiramo setnju
max=-8
for i in range(0,n+1):
    for j in range (0,m+1):
       if sm[i][j]>max: 
        max=sm[i][j] 
        r=i
        z=j
setnja=[]
broj=-1
i=r
j=z
while (sm[i][j]!=0):
    setnja.append ((i,j)) 
    (i,j)=novi[i][j] 
    broj+=1
## trazenje odgovarajucih poravnanja 
k=broj
min=-8

niz1=""
niz2=""
if (broj==-1):
    for i in range(0,n): 
        for j in range(0,m):
            if (bm[ak.index(y[i])][ak.index(x[j])]>min): 
                min=bm[ak.index(y[i])][ak.index(x[j])] 
                niz1=x[j]
                niz2=y[i]
while (broj!=-1):
    if ((i+1,j)==setnja[broj]):
    niz2+=(y[i])
    niz1+=('-') 
    i+=1
if ((i,j+1)==setnja[broj]): 
    niz1+=x[j]
    niz2+=('-')
    j+=1
if ((i+1,j+1)==setnja[broj]):
    niz2+=y[i] 
    niz1+=(x[j]) 
    i+=1
    j+=1
broj-=1
print niz1 
print niz2
