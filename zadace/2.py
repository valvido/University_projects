f1=open("PAM1matrix.txt","r")
PAM1matrix=[]

for i in range(20):
    line=f1.readline()
    vec=line.split()
    PAM1matrix.append(vec[:])
f1.close()

for i in range(20):
    for j in range(20):
        PAM1matrix[i][j]=float(PAM1matrix[i][j])

for i in range(20):
    for j in range(20):
         PAM1matrix[i][j]=PAM1matrix[i][j]/10000

def mnozenje (A, B):
    redA = len(A)
    stupacA = len(A[0])
    redB = len(B)
    stupacB = len(B[0])

    if stupacA != redB:
      return
    
    C = [[0 for red in range(stupacB)] for stupac in range(redA)]
    for i in range(redA):
        for j in range(stupacB):
            for k in range(stupacA):
                C[i][j] += A[i][k] * B[k][j]
    return C

umn=PAM1matrix
for i in range(999):
    umn = mnozenje (umn, PAM1matrix)



for i in range(20):
    print(umn[i])
    
