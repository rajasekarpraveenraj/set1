N=int(input("enter the number of elements in an array"))
array=[]
for i in range(0,N):
    array.append(int(input()))
array.sort()#sorting an array
a=len(array)//2
print("The median element in the given array is",array[a])
