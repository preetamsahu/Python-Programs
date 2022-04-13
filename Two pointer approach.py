'''
tow pointer approach to check if a string is a palindrome and find target value in a sorted array
'''
def ispalindrome(s):
    #start
    i=0
    #end
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return 0
        i+=1
        j-=1
    return 1
# t=int(input())#The number of test cases
# for i in range(t):
#     s=input()
#     print(ispalindrome(s))
def