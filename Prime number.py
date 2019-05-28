number=int(input())
i=2
while(i<number):
    if(number%i==0):
        break
    i+=1
if(number==i):
    print("True")
elif(number==1):
    print("Neither prime nor composite")
else:
    print("False")
