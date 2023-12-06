import math

f1=open("acids.txt", "r") 
aco=f1.readline()
f1.close()

f1=open("blosum50.txt", "r")
bm=[]
for i in range(20):
    line=f1.readline()
    wc=line.split()
    bm.append(wc[:])
f1.close()

for i in range(20):
    for j in range(20):
        bm[i][j]=int(bm[i][j])

def ss(x,y):
    m=len(x)
    n=len(y)
    tab=[]
    tmp=[]
    
    for i in range(m+1):
        tmp.append(0)
    for i in range(n+1):
        tab.append(tmp[:]) #inicijalizacija

    for i in range(n+1):
        tab[i][0]=math.exp(-8*i)
    for i in range(m+1):
        tab[0][i]=math.exp(-8*i) #rubne vrijednosti
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            tab[i][j]=math.exp(-8)*tab[i-1][j]+math.exp(-8)*tab[i][j-1]+math.exp(bm[aco.index(y[i-1])][aco.index(x[j-1])]) * tab[i-1][j-1]
    return tab[n][m]

x="HPEW"
y="PW"
ss0=ss(x,y)
print "statisticka suma od HPEW i PW:"
print ss0

x='EW'
y='W'
ss1 = ss(x,y)

SS1 = math.exp(-8) * math.exp(bm[aco.index('P')][aco.index('P')]) * ss1

p = SS1 / ss0

print "vjerojatnost da je P poravnat sa sobom:"
print p

x='HPE'
y='P'
ss2 = ss(x,y)

SS2 = ss2 * math.exp(bm[aco.index('W')][aco.index('W')])

w = SS2 / ss0

print "vjerojatnost da je W poravnat sa sobom:"
print w


            
        
