def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    
    n = len(arr)
    lis = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    return max(lis)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(arr))
