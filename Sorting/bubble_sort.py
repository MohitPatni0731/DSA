# Bubble Sort
"""
Time - O(N^2)
Space - O(!)
"""
arr = [1, 4, 3, 2]

for i in range(len(arr)):
    for j in range(1, len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)  # Output - [1, 2, 3, 4]
