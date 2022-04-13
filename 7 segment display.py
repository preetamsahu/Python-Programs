N=int(input())
S=input()
seven_seg={'0':6,'1':2,'2':5,'3':5,'4':4,'5':5,'6':6,'7':3,'8':7,'9':5}
segment_seg_num=[6,2,5,5,4,5,6,3,7,5]
segment=0
for i in S:
    segment+=seven_seg[i]
i=0
j=0
smallest_num=''
while i<N:
    segment-=seven_seg[str(j)]
    if segment<seven_seg['1']*(N-i-1):
        segment+=seven_seg[str(j)]
        j+=1
    else:
        smallest_num+=str(j)
        i+=1
print(smallest_num)

