class Lower:
    def lower_bound(arr, target):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        return l
