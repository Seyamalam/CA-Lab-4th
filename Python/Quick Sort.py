def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


arr = list(map(int, input("Enter the array: ").split()))
print(f"Sorted array: {quick_sort(arr)}")
