# In selection sort we select a minimum element form the unsorted array in evenry itration and put them into at the beginning it maintains two types of
# array sorted array as well as unsorted
array=[1,4,7,3,2,56,23,56,3,2]
sorted_array=list()
for i in range(len(array)):
    index=i
    for j in range(i+1,len(array)):
        if array[i]>array[j]:
            index=j
    array[i],array[index]=array[index],array[i]
print(array)

