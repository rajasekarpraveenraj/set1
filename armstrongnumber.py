n=int(input("enter the number: "))
temp=n
sum1=0
while n!=0:
    rem=n%10
    sum1=(pow(rem,3))+sum1
    n=n//10
if sum1==temp:
    print("yes")
else:
    print("no")
    
