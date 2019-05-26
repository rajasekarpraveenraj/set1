#PF-Exercise Assignment 26
#Chinese puzzle
heads=150
legs=400
if(legs%2==0):
    count=legs/2
    rabbits=count-heads
    hens=heads-rabbits
else:
    print("No solution")
print(rabbits)
print(hens)

