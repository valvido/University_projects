import random
f=open("brojuspjeha.txt", "w")
for o in range(1000):
    n=[]
    for i in range(100):
        n.append(random.randint(0,1))
    
    mx=0
    c=0

    for i in range(100):
        if (n[i]==1):
            c=c+1
            if(c>mx):mx=c
        else: c=0
    #print(n)
    #print(mx)
    if(i !=999): f.write('{0} '.format(mx))
    else: f.write('{0}'.format(mx))
