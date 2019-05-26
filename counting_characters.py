c=input("enter the sentence")
count=0
for i in range(0,len(c)):
    if c[i]!=" ":
        count+=1
print("Number of characters",count)
