# Nije moj program, ja sam samo dodao komentare

# ovo je generalizirano rjesenje

# cesto se koriste for petlje s range-om: len(emisija)
# u nasem konkretnom primjeru je len(emisija) = 2 jer imamo dva stanja (Postena kocka i Nepostena kocka)
# u "viterbi.py" zato ne koristimo for petlje za setanje po retcima jer ih imamo samo 2, a posto
# se stupci obradjuju paralelno imamo samo naredbe tipa:
# 	M[0][i] = nesto
# 	M[1][i] = nesto
# tj. redaka imamo samo dva, to su: M[0] i M[1] (Postena/Nepostena kocka), a stupaca imamo proizvoljno mnogo
# -> broj stupaca je jednak duljini niza x kojeg korisnik zadaje proizvoljno

# ovdje su i retci i stupci varijabilni (dakle korisnik moze zadati proizvoljno mnogo stanja i proizvoljno dug niz)
# npr. korisnik smije modificirati datoteke "kocke_e.txt" i "kocke_t.txt" tako da ima 5 kocki, a ne samo dvije i
# program ce raditi ispravno (uz uvjet da je korisnik korektno modificirao datoteke za emisijske/tranzicijke vjerojatnosti)

import sys

f = open("kocke_e.txt", "r")
emisija = []
for line in f:
    emisija.append(line.split())

for i in range(len(emisija)):
    for j in range(len(emisija[i])):
        emisija[i][j] = float(emisija[i][j])

f.close()

f = open("kocke_t.txt", "r")
tranz = []
for line in f:
    tranz.append(line.split())

for i in range(len(tranz)):
    for j in range(len(tranz[i])):
        tranz[i][j] = float(tranz[i][j])

f.close()

x ="123455666666123452"

def viterbi(x, emisija, tranz):
    n = len(x)
    dp = {}
	
    b = 1.0 / len(emisija)		# konkretno za nas primjer s dvije kocke: "b = 1.0 / 2 = 0.5"
	# na samom pocetku odabiremo kocku s kojom cemo bacati tj. u tzv. inicijalnom stanju smo
	# vjerojatnost da cemo uzeti postenu kocku je 0.5 = b
	# vjerojatnost da cemo uzeti nepostenu kocku je 0.5 = b
	
	# da smo imali 3 kocke onda bi b bio 1/3 tj. 0.333333... pa bi odabir bilo koje od 3 kocke imao vjerojatnost 0.333333...
	# -> tranzicijske vjerojatnosti opisuju samo situacije kada prelazimo s vec odabrane kocke na neku drugu ili istu kocku
	# tj. opisuju prijelaz iz jednog stanja iz skupa mogucih stanja u drugo ili isto stanje 
	# no ne opisuju vjerojatnosti da se na pocetku nalazimo u nekom od tih stanja
	
	# pa je ideja da se elementi nultog stupca matrice (koji opisuju vjerojatnosti emitiranja prvog simbola iz niza x)
	# izracunaju tako da se "vjerojatnost emisije simbola" pomnozi s vjerojatnoscu da smo se inicijalno nasli u stanju
	# koje opisuje dani redak, a tu vjerojatnost smo definirali tako da je za sva stanja ista tj. jednaka je b
	# -> svaki element nultog stupca se dobije tako da se odgovarajuca emisijska vjerojatnost pomnozi sa b
    for i in range(len(emisija)):
        dp[(i, 0)] = b * emisija[i][int(x[0]) - 1]		# mnozenje sa b nije nuzno, moze se staviti samo: " dp[(i, 0)] = emisija[i][int(x[0]) - 1] "
	
	# NAPOMENA 
	# mnozenje sa b se moze potpuno izbaciti, rezultat programa ce biti isti
	# razlog tome je sam algoritam u kojem se elementi matrice racunaju na temelju elemenata iz prethodnih stupaca
	# i to samo operacijom mnozenja pa ce se b javiti kao skalar u svakom elementu matrice tocno jednom
	# svaki element matrice (osim onih u nultom stupcu) se moze rastaviti na sastavne dijelove:
	#	element iz prethodnog stupca * tranzicijska vjerojatnost * emisijska vjerojatnost
	# a posto se elementi prvog stupca racunaju na temelju elemanata iz nultog stupca (njih smo pomnozili sa b)
	# moci cemo iz elemenata prvog stupca izluciti b, dalje se elementi drugog stupca racunaju iz elemenata
	# prvog stupca (koji imaju faktor b u sebi) pa cemo i iz elemenata drugog stupca moci izluciti b
	# -> b se dakle "propagira" kroz cijelu matricu pa ga na kraju mozemo izluciti kao skalar
	# to ne kvari rezultat jer je b pozitivan, a i svi elementi matrice su pozitivni (nastali su iz vjerojatnosnih vrijednosti)
	
    for i in range(1, n):
        for j in range(len(emisija)):
            dp[(j, i)] = emisija[j][int(x[i]) - 1];
            max_prev = 0.0;
            for k in range(len(emisija)):
                if tranz[k][j] * dp[(k, i - 1)] > max_prev:
                    max_prev = tranz[k][j] * dp[(k, i - 1)]

            dp[(j, i)] *= max_prev

    path = [0]
    for i in range(1, len(emisija)):
        if dp[(path[0], n - 1)] < dp[(i, n - 1)]:
            path[0] = i

    pos = n - 2 
    while pos > -1:
        for i in range(len(emisija)):
            if emisija[path[0]][int(x[pos + 1]) - 1] * (tranz[i][path[0]] * dp[(i, pos)]) == dp[(path[0], pos + 1)]:
                path = [i] + path
                break
        pos -= 1
     
    return  path



res = ""
for i in viterbi(x, emisija, tranz):
    if i == 0:
        res += 'F'
    else:
        res += 'L'

print res
