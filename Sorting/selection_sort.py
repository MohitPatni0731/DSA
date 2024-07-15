# Selection Sort
"""
Time - O(N^2)
Space - O(1)
"""
arr = [2, 1, 3, 4]
for i in range(len(arr)):
    curr_min = i
    for j in range(i + 1, len(arr)):
        if arr[j] < arr[curr_min]:
            curr_min = j
    arr[i], arr[curr_min] = arr[curr_min], arr[i]
print(arr)  # Output - [1, 2, 3, 4]
