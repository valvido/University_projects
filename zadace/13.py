f1=open("avermitilisProteom001.txt", "r")
d=int(f1.readline())

x=[]
for i in range(d):
	line=f1.readline()
	vector=line.split()
	x.append(vector)

print x

##for i in range (2045):
  ##  for j in range (len(
