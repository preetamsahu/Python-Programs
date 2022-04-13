
X=int(input())
numbers=list(map(int,input().split()))
for i in range(len(numbers)):
    numbers[i]=str(numbers[i])
cnt=0
sett=list(set(numbers))
print(sett)
for i in range(len(sett)-1):
    for j in range(i+1,len(sett)):
        from math import perm
        num1="".join([sett[i],sett[j]])
        num2="".join([sett[j],sett[i]])
        K=numbers.count(sett[i])
        J=numbers.count(sett[j])
        if int(num1)==X or int(num2)==X:
            cnt=cnt+K*J
        if int(num1) == int(num2)==X:
            cnt+=K*J
print(cnt)
for i in sett:
    if numbers.count(i)>1:
        if X==int("".join([i,i])):
            k = numbers.count(i)
            fact = 1

            for i in range(1, k + 1):
                fact = fact * i
            print(k,fact)
            cnt = cnt + fact // 2
print(cnt)

'''
1212
1 212 12 12
3

11011
11 11 110

333
3 33 18

743
17 17 74 15 22 29 7 16 14 6

ma
20
'''
