import collections
def ispali(s):
    # TODO string[::-1] gives the reverse of string
    if s==s[::-1]:
        return 1
    else:
        return 0
def anagram1(s1,s2):
    #TODO it has time coplexity O(nlogn)
    if sorted(s1)==sorted(s2):
        return 1
    else:
        return 0
def anagram2(s1,s2):
    cnt1=collections.Counter(s1)
    cnt2=collections.Counter(s2)
    if cnt1==cnt2:
        return 1
    else:
        return 0
    #collections.Counter convert string in dictionary and make key pari where key is element and value is the number of count that it occurre
t=int(input())
while t:
    t-=1
    string=input()
    print(ispali(string))


