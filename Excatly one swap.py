S=input()
ans = []
def calc(num):
    return num*(num-1)//2
def ExactlyOneSwap(S):
    if len(S) == len(set(list(S))):
        print(calc(len(S)))
    else:
        freq = []
        lst = list(S)
        for i in set(lst):
            freq.append(lst.count(i))
        sum = calc(len(S))
        for i in freq:
            if i > 1:
                sum = sum - calc(i)
        print(sum + 1)

#This is bruteforce approach
for i in range(len(S)-1):
    p = 0
    lst = list(S)
    key = lst[i]
    for j in range(i+1, len(S)):
        if key==lst[j] and p==0:
            p+=1
        elif key==lst[j] and p>0:
            continue
        lst = list(S)
        lst[i] = lst[j]
        lst[j] = key
        lst = "".join(lst)
        ans.append(lst)
print(len(set(ans)))
ExactlyOneSwap(S)