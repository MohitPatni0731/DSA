s = "anagram"
t = "nagaram"
array1 = sorted(char for char in s)
array2 = sorted(char for char in t)

if array1 == array2:
    return True
else:
    return False

