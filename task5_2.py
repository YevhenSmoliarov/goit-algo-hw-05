def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])
        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1
    
    # If we haven't found an exact match, upper_bound is the smallest element greater than the target
    return (iterations, upper_bound)

# Приклад використання
arr = [0.1, 0.5, 1.3, 2.7, 3.3, 4.4, 5.6, 6.9]
target = 3.5

result = binary_search(arr, target)
print(f"Ітерації: {result[0]}, Верхня межа: {result[1]}")