def get_all_indices(string, delim):
    indices = []
    for (i, s) in enumerate(string):
        if s == delim: indices.append(i)
    return indices

def get_all_substrs(input):
    # to accumalate strings
    l = []
    input = input.strip()
    open_indices = get_all_indices(input, '(')
    close_indices = get_all_indices(input, ')')

    for i in open_indices:
        for j in close_indices:
            l.append(input[i:j+1])

    return l

def validate(inp):
    stack = []

    try:
        for i in inp:
            if i == '(': stack.append(1)
            elif i == ')': stack.pop()

        return len(stack) == 0
    except:
        return False

inp = input()
print("All substrs: \n", get_all_substrs(inp))
print("Anss")
try:
    print(max(map(len, filter(validate, get_all_substrs(inp)))))
# stack=[]
# top=-1
# cnt_current=0
# cnt_prv=0
# for i in range(len(S)):
#     if S[i]=='(':
#         stack.append(S[i])
#         top+=1
#         cnt_prv=0
#     else:
#         if len(stack)==0:
#             cnt_prv=0
#         else:
#             cnt_prv+=2
#             cnt_current+=2
#             cnt_current=max(cnt_prv,cnt_current)
#             stack.pop()
#             top-=1
#
# print(cnt_current)