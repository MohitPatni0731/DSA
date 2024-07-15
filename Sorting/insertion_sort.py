# Insertion Sort
"""
Time - O(N^2)
Space - O(1)
"""
arr = [2, 1, 4, 3]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
print(arr)
