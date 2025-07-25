def two_sum_sorted(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
    if current_sum == target:
            return[left,right]
    elif current_sum < target:
            left += 1
    else:
            right -= 1
    return[-1, -1]
        
arr = [2,4,5,7,8]
target = 9
print(two_sum_sorted(arr,target))