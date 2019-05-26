n=int(input("starting limit: "))
s=int(input("ending limit: "))
for i in range(n,s+1):
    sum1=0
    temp=i
    while i!=0:
        rem=i%10
        sum1=(pow(rem,3))+sum1
        i=i//10
    if sum1==temp:
         print(sum1)
    
