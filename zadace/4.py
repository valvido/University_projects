f1=open("acids.txt", "r") 
ak=f1.readline()
f1.close()

bm=[] 

f1=open("blosum50.txt", "r")

for i in range(20):
    line=f1.readline()
    vc=line.split()
    bm.append(vc[:])
for i in range(20):
    for j in range(20):
        bm[i][j]=int(bm[i][j])

f1.close()
		
def score(a, b):
	
	score = 0

	for i in range(len(a)):
		if(a[i] == '_' or b[i] == '_'): score = score - 8
		else: score = score + bm[ak.index(a[i])][ak.index(b[i])]
			
	return score


niz1 = "HPEWAAKEGHI"
niz2 = "PWALVNGSE"

L1 = len(niz1)
L2 = len(niz2)


poravnanje = [0]*L1 + [1]*L2

def ubaci_crtice(n):
	
	m = []	
	
	if(n[0] == 1): m.append('_')	
									
	
	for i in range(len(n) - 1):
		m.append(str(n[i]))
		if(n[i] == n[i+1]): m.append('_')	
			
	m.append(str(n[len(n)-1]))
	if(n[len(n)-1] == 0): m.append('_')		
											
	return m
	
def ispis_poravnanja(p):
	

	n1 = ''
	n2 = ''
	
	k = 0
	l = 0
	
	for i in range(len(p)/2):

		if(p[2*i] == '0'):
			n1 = n1 + niz1[k]
			k = k + 1
			
		else: n1 = n1 + '_'

		if(p[2*i + 1]) == '1':
			n2 = n2 + niz2[l]
			l = l + 1
			
		else: n2 = n2 + '_'
			
	print(n1)
	print(n2)
	print("\n score = {0}".format(score(n1,n2)))
	
	
import random

for i in range(100):
	random.shuffle(poravnanje)
	print(poravnanje)
	print('')
	p = ubaci_crtice(poravnanje)
	ispis_poravnanja(p)
	print('\n')
