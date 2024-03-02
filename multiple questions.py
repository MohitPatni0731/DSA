'''nums = [1,1,2,3]
nums.sort()  # Sort the array (optional depending on the problem requirements)
slow = 0  # Slow pointer starting from the beginning
for fast in range(1, len(nums)):  # Fast pointer starting from the second element
    print(nums[slow], "::", nums[fast])
    slow += 1'''
    
'''nums = [1, 1, 2, 3, 4, 5, 6]
nums.sort()  # Sort the array (optional depending on the problem requirements)
slow = 0  # Slow pointer starting from the beginning
fast = len(nums) - 1  # Fast pointer starting from the end

while slow < fast:  # Continue until slow pointer meets or passes fast pointer
    print(nums[slow], "::", nums[fast])
    slow += 1
    fast -= 1'''

'''
s = "anagam"
t = "nagaram"
if sorted(s) == sorted(t):
    print(True)
else:
    print(False)
#print(sorted(s))
#print(sorted(t))'''

'''
nums = [2, 11, 7, 15]
target = 9
index = []  # Store the indices of the two numbers that sum up to the target
slow = 0  # Slow pointer starting from the beginning

for fast in range(1, len(nums)):  # Fast pointer starting from the second element
    current_sum = nums[slow] + nums[fast]
    if current_sum == target:
        index.append(nums.index(nums[slow]))
        index.append(nums.index(nums[fast]))
        break  # Stop the loop if the indices are found

print(index)'''


"""l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
#for ele in enumerate(l1):
#	print (ele)

# changing index and printing separately
#for count, ele in enumerate(l1, 100):
#	print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)
"""

'''nums = [3, 2, 4]
target = 6
array = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            array.append(i)
            array.append(j)
            print(array)'''
            
'''           
s = "A man, a plan, a canal: Panama"   
def remove_all_chars_except_alphanumeric(text):
  import re
  return re.sub(r"[^\w]", "", text)


result = remove_all_chars_except_alphanumeric(s.lower())

left, right = 0, len(result) - 1
while left < right:
    if result[left] != result[right]:
        return False
    left += 1
    right -= 1
return True'''


'''
t = int(input())
increment = 1
decrement = t * (t + 1) // 2
for i in range(1,t+1):
    for j in range(1, i+1):
        print(increment, end=" ")
        increment += 1
    print()
for i in range(t - 1, 0, -1):
        for j in range(i):
            print(decrement, end=" ")
            decrement -= 1
        print()'''


s = "(()())(())"
for i in s:
    print(i)