class Upper:
    def upper_bound(arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l
