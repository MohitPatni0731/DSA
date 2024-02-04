pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
stack = []
for i in pushed:
    stack.append(i)
    if stack[-1] == popped[0]:
        stack.pop()
    else:
        pass
if len(stack) == 0:
    print(True)
else:
    print(False)