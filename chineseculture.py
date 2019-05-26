#PF-Exer 21-level 2
#Chinese_culture_of_luck(i.e.,sum of digits of a registration number should be 9)

registration_number=9099
sum_of_digits=0
sum_of_digits1=0
while(registration_number!=0):
    rem=registration_number%10
    sum_of_digits=rem+sum_of_digits
    registration_number=registration_number//10
if(sum_of_digits<=9):
    if(sum_of_digits==9):
        print("The rgistration_number is found to be lucky",sum_of_digits)
    else:
        print("The rgistration_number is found to be unlucky",sum_of_digits)
else:
    while(sum_of_digits!=0):
        rem1=sum_of_digits%10
        sum_of_digits1=rem1+sum_of_digits1
        sum_of_digits=sum_of_digits//10
    if(sum_of_digits1==9):
        print("The rgistration_number is found to be lucky",sum_of_digits1)
    else:
        print("The rgistration_number is found to be unlucky",sum_of_digits1)
