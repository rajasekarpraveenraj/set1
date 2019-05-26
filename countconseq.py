#PF-Exer-18
#count of adjacent occurences
a=[1,1,5,100,-20,-20,6,0,0]
b=len(a)-1
count=0
for i in range(0,b):
    if(a[i]==a[i+1]):
        count=count+1 

print(count)
       
