from collections import defaultdict

x=input()
stack = []
top = -1
for i in range(len(x)):
    if x[i] == '}' and top == -1 or x[i] == '}' and top == -1 or x[i] == ']' and top == -1:
        print(stack, i)
        print("False")

    elif x[i] == '{' or x[i] == '(' or x[i] == '[':
        print(stack, i)
        stack.append(x[i])
        top += 1

    elif (x[i]=='}' and stack[top]=='{'):
        k=stack.pop()
        print(stack, i, "HEYYYYYYYYYYY", k)
        top -= 1

    elif (x[i]==')' and stack[top]=='('):
        k = stack.pop()
        print(stack, i, "HEYYYYYYYYYYY", k)
        top -= 1
    elif (x[i]==']' and stack[top]=='['):
        k = stack.pop()
        print(stack, i, "HEYYYYYYYYYYY", k)
        top -= 1
    else:
        print(0,"YESSSS")
if len(stack) == 0:
    print("True")
else:
    print( "False")