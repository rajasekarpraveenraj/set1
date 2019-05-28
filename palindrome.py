num=int(input())
temp=num
sum1=0
while temp!=0:
    rem=temp%10
    rev=rem*10+sum1
    temp=temp//10
print(rev)
if (rev==num):
    print("yes")
else:
    print("no")
