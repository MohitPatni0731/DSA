'''
1.
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,'''

'''Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''

expense_list = [
    ("January", 2200),
    ("February", 2350),
    ("March", 2600),
    ("April", 2130),
    ("May", 2190)
]

#SOLUTION 1
#print("In Feb,",expense_list[1][1]-expense_list[0][1], "more dollars spent then January.")

#SOLUTION 2
#print("Total expenses in the first quater of the year is :",expense_list[0][1]+expense_list[1][1]+expense_list[2][1],"$.")

#SOLUTION 3
'''for month, expense in expense_list:
    if expense == "2000":
        print("Found the match")
        break
    else:
        print("Not found")'''
        
#SOLUTION 4
#expense_list.append(("June", 1980)) print(expense_list)

#SOULUTION 5
'''April_expense=expense_list[3][1]
expense_list[3] = ("April", April_expense - 200)
print(expense_list)'''


'''
2.
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)'''

heros=['spider man','thor','hulk','iron man','captain america']

#SOULTION 1
#print(len(heros))

#SOLUTION 2
#heros.append('black panther')

#SOLUTION 3
#heros.pop(5)
#heros.insert(3,'black panther')

#SOLUTION 4
'''for hero in heros[:]: 
    if hero == 'hulk' or hero == 'thor':
        heros.remove(hero)'''

#SOLUTION 5
#heros.sort()
#print(heros)

'''
3.
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
'''
'''
input = int(input("Enter a maximum number - "))
list = []
for i in range(input+1):
    if i%2 == 1:
        list.append(i)
print(list)'''

