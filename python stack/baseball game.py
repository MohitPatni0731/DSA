operations = ["5","2","C","D","+"]
record = []
for i in operations:
    try:
        score = int(i)
        record.append(score)
    except ValueError:
        if i == "C":
            record.pop()
        elif i == "D":
            record.append(2*(record[-1]))
        elif i == "+":
            record.append(record[-1]+record[-2])
print(sum(record))
                
#int, C means last score pop out, D means previous score ka double,+ means abhi last 2 things stack main hai usko add karke likh do
            
