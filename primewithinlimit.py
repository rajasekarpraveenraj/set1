n=int(input("starting limit: "))
e=int(input("ending limit: "))
for j in range(n,e+1):
    i=2
    while(i<j):
        if(j%i==0):
            break
        i+=1
    if(j==i):
        print(j)
