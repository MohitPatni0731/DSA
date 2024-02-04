s = "({)"
brackets = {"(":")", "[":"]", "{":"}"}
stack = []
for i in s:
    if i == "(" or i == "[" or i == "{":
        stack.append(i)
    else:
        if len(s) == 0:
            print(False)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                print(False)
                
if len(stack)==0:
    print(True)
else:
    print(False)