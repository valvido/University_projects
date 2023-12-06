f=open("avermitilisProteom001.txt", "r")
x="FVFGDSLSDA"

n=2045

for i in range(n):
    y=x
    line=f.readline()
    duljina=len(y)
    mjesto=0
    max=0

    for j in range (len(line)):
        br=0
        if (mjesto+duljina)>len(line): break
        st=line[mjesto:mjesto+duljina]

        for k in range (duljina):
            ind=k
            if (st[ind]==y[ind]):
                br=br+1

        if (br>max):
            max=br
        mjesto=mjesto+1

    print max
    
f.close()
