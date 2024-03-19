s = "(())" 
open = []
score = 0 
for i in s:
    if i == "(":
        open.append(score)
        score = 0
    else:
        score = open.pop() + max(2 * score, 1)
#print(score)