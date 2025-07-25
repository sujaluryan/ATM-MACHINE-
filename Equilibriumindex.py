def equilibrium_index(arr):
    total = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == (total - left_sum - arr[i]):
          return i
        left_sum += arr[i]
    return -1

print(equilibrium_index([1,3,5,7]))