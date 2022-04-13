'''
IV IX
XL XC
CD CM
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
LVIII
'''
romen={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input()
s=list(s)
s.reverse()
s="".join(s)#reverse the string
sum=0
condi=0
i=0
while i<len(s):
    if i<(len(s)-1):
        if romen[s[i]]>romen[s[i+1]]:
            sum=sum+romen[s[i]]-romen[s[i+1]]
            i+=1
            i+=1
        else:
            sum=sum+romen[s[i]]
            i+=1
    else:
        sum = sum + romen[s[i]]
        i += 1
print(sum)
