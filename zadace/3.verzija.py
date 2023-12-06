# Analiza Viterbijevog algoritma (ima li njegov output smisla?)
# viterbi_1.png, ... , viterbi_6.png

# funkcija upis() upisuje matricu vjerojatnosti u datoteku "matrice2.txt"
def upis(niz, stupac, M, L):
	
	f = open("matrice2.txt", "w")
	
	f.write("e{0}".format(niz[0].rjust(15)))
	for i in range(1,L):
		f.write("{0}".format(niz[i].rjust(32)))
	f.write("\n")

	# prvi redak matrice vjerojatnosti
	f.write("{0} ".format(stupac[1]))
	f.write("%.20f " % M[0][0])
	for i in range(1,L):
		if(M[0][i-1] * stanjeP * postenaKocka[int(niz[i])-1] == M[0][i]):
			f.write("  v_P  - %.20f " % M[0][i])
		else: f.write("  v_NP - %.20f " % M[0][i])
		
	f.write('\n')

	# drugi redak matrice vjerojatnosti
	f.write("{0} ".format(stupac[2]))
	f.write("%.20f " % M[1][0])
	for i in range(1,L):
		if(M[1][i-1] * stanjeN * nepostenaKocka[int(niz[i])-1] == M[1][i]):
			f.write("  v_N  - %.20f " % M[1][i])
		else: f.write("  v_PN - %.20f " % M[1][i])
		
	f.write('\n')
	
	f.write("i{0}".format('0'.rjust(15)))
	for i in range(1,L):
		f.write("{0}".format(str(i).rjust(32)))
	f.write("\n\n")
	
	f.write("e = element niza x = {0}\n".format(x))
	f.write("i = indeks elementa niza\n")
	f.write("P = stanje P(ostena kocka)   N = stanje N(epostena kocka)\n\n")
	f.close()
	
def max(x, y):
	if(x >= y): return x
	return y

tranzicijske_vjerojatnosti = open("kocke_t.txt", "r")
emisijske_vjerojatnosti = open("kocke_e.txt", "r")

s1 = tranzicijske_vjerojatnosti.readline()
s2 = tranzicijske_vjerojatnosti.readline()

stanjeP = float(s1.split()[0])
prijelaz_P_u_N = float(s1.split()[1])
prijelaz_N_u_P = float(s2.split()[0])
stanjeN = float(s2.split()[1])

print ("Vjerojatnost da smo nakon bacanja postene kocke ponovno uzeli postenu kocku je: "),stanjeP
print ("Vjerojatnost da smo nakon bacanja postene kocke uzeli nepostenu kocku je: "),prijelaz_P_u_N
print 
print ("Vjerojatnost da smo nakon bacanja nepostene kocke ponovno uzeli nepostenu kocku je: "),stanjeN
print ("Vjerojatnost da smo nakon bacanja nepostene kocke uzeli postenu kocku je: "),prijelaz_N_u_P
print

s1 = emisijske_vjerojatnosti.readline()
s2 = emisijske_vjerojatnosti.readline()

postenaKocka = []
nepostenaKocka = []

for i in range(6):
	postenaKocka.append(float(s1.split()[i]))
	nepostenaKocka.append(float(s2.split()[i]))
	
print
print("Prilikom bacanja kocke je pao broj:         1      2      3      4      5      6")
print("Emisijske vjerojatnosti postene kocke:   "),
for i in range(6):
	print("%.3f " % postenaKocka[i]),
print
print("Emisijske vjerojatnosti nepostene kocke: "),
for i in range(6):
	print("%.3f " % nepostenaKocka[i]),
print '\n\n'

tranzicijske_vjerojatnosti.close()
emisijske_vjerojatnosti.close()	
	
	
# za dani niz pokusavamo otkriti kako je on nastao (tj. kako je najvjerojatnije nastao - ne znamo tocno!)
# u ovom zadatku nas zanima je li pojedini element niza dobiven bacanjem postene ili nepostene kocke
# to ne mozemo tocno odrediti, ali mozemo za svaki element odrediti kako je najvjerojatnije dobiven
# tj. koja stanje je najvjerojatnije proizvelo emisiju pojedinog elementa niza

x ="123455666666123452"		# niz koji promatramo

L = len(x)
niz = []		# u ovu matricu cemo spremiti pojedine elemente niza x
stupac = []		# ovo sluzi samo za ljepsi ispis matrice (da znamo koji redak se odnosi na koje stanje (postena/nepostena kocka))
tmp = []
M = []			# matrica vjerojatnosti za odredjivanje optimalnog prolaza niza kroz model

for i in range(L):
	niz.append(x[i])
	
stupac.append('S\N')	 # S = stanje (moguca stanja su u stupcu ) ; N = niz (elementi niza x su u retku)
stupac.append('P  ')
stupac.append('N  ')

for i in range(L):
	tmp.append(0.0)

for i in range(2):
	M.append(tmp[:])

# emisija prvog znaka
M[0][0] = postenaKocka[int(niz[0])-1]
M[1][0] = nepostenaKocka[int(niz[0])-1]


# punjenje matrice M prema formuli Viterbijevog algoritma
for i in range(L-1):
	
	a = M[0][i] * stanjeP
	b = M[1][i] * prijelaz_N_u_P
	M[0][i+1] = max(a, b) * postenaKocka[int(niz[i+1])-1]
	
	a = M[1][i] * stanjeN
	b = M[0][i] * prijelaz_P_u_N
	M[1][i+1] = max(a, b) * nepostenaKocka[int(niz[i+1])-1]

upis(niz, stupac, M, L)

prolaz = ''

i = L - 1

# traceback (analogno traceback-u za score matricu - Zad 2)
# trazimo koji prolaz je dao maksimalnu vjerojatnost
while(i > -1):
	
	if(i == L - 1):
		# pocinjemo od zadnjeg stupca -> odredimo vecu od dvije vrijednosti u tom stupcu
		# 	ako je veca vrijednost u 0. retku -> stanje P je vjerojatnije, u suprotnom je stanje N vjerojatnije
		if( M[0][i] >= M[1][i]): prolaz = 'P'
		else: prolaz = 'N'
			
	else:
		
		# zatim od kraja prema pocetku (od predzadnjeg stupca prema nultom stupcu (zadnji stupac smo rjesili u prethodnom if-u))
		#	odredjujemo koje stanje je "proizvelo" ono iduce stanje (trazimo optimalni put unatrag)
		
		if(prolaz[0] == 'P'):	# iduce stanje je P
			if(M[0][i] * stanjeP * postenaKocka[int(niz[i+1])-1] == M[0][i+1]): prolaz = 'P' + prolaz
			else: prolaz = 'N' + prolaz
				
		else:	# iduce stanje je N
			if(M[1][i] * stanjeN * nepostenaKocka[int(niz[i+1])-1] == M[1][i+1]): prolaz = 'N' + prolaz
			else: prolaz = 'P' + prolaz
				
	i = i - 1

print ("Optimalni prolaz niza \"{0}\" kroz povremeno nepostenu kockarnicu je: {1}\n".format(x, prolaz))	
print ("P = bacali smo postenu kocku	N = bacali smo nepostenu kocku\n")
