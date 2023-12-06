f=open("acids.txt","r")
kiseline = f.readline()
f.close()

print("Kiseline: {0}\n".format(kiseline))

f=open("blosum50.txt","r")
blosum=[]

for i in range(20):
	redak = f.readline()
	razdvojeno = redak.split()
	blosum.append(razdvojeno[:])

f.close()
	
for i in range(20):
	for j in range(20):
		blosum[i][j]= int(blosum[i][j])
		
for i in range(20):
	print(blosum[i])
	
print("\n")

f=open("por001.txt")

niz = f.readline()
poravnanje = f.readline()
niz=niz.rstrip('\n')
poravnanje=poravnanje.rstrip('\n')
f.close()

print("Prvi niz: {0}".format(niz))
print("Drugi niz: {0}\n".format(poravnanje))

l = len(niz)
print("Duljina niza: {0}\n".format(l))

score = 0

for i in range(l):
	if(poravnanje[i] == '_' or niz[i] == '_'): score = score - 8
	else: score = score + blosum[kiseline.index(poravnanje[i])][kiseline.index(niz[i])]
	
print("Score: {0}\n".format(score))
