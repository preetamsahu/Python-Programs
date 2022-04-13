N=int(input())
S=input()
seven_seg={'0':6,'1':2,'2':5,'4':4,'7':3,'8':7}
segment_req=[6,2,5,5,4,5,6,3,7,]
seg=0
for i in S:
    seg+=seven_seg[i]
num=[2]*N
sum=seg-2*N
while sum>