given_year=int(input())
if given_year%4==0:
   if given_year%100==0:
       if given_year%400==0:
           print("Leap year")
       else:
           print("Not a leap year")
   else:
       print("Leap year")
else:
    print("Not a leap year")
