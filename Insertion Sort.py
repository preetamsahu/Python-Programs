# insertion sort is similar to sorting the playing cards in your hands. in this algorithm array is virtually split into sorted and unsorted array. element
# form the unsorted picked and placed in sorted array at the correct position
array=[4,2,1,7,34,5,5,3,67,7,7,7,89,9,4,2,3,6,23,4]
for i in range(1,len(array)):
    j=i-1
    while j>=0 and array[j+1]<array[j]:
        array[j],array[j+1]=array[j+1],array[j]
        j-=1
        print(True)

    print(array,)
print("Sorted array ::::::",array)