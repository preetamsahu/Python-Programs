#in bubbel sort algorithm what we do we repeatedly swap adjecent element if they are in worng order
array=[9,8,7,6,5,4,3,2,1]
for i in range(len(array)):
    for j in range(len(array)-1-i):
        if array[j]>array[j+1]:
            array[j] , array[j+1]=array[j+1],array[j]

print(array)
