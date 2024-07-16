# Bubble Sort
class Bubble:
    def bubble_sort(arr):
        """
        Time - O(N^2)
        Space - O(!)
        """
        for i in range(len(arr)):
            for j in range(1, len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
