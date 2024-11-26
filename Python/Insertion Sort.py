def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"Step-{i} -> {arr}")


arr = [5, 4, 8, 3, 6]
print(f"Original array: {arr}")
insertion_sort(arr)
print(f"The final sorted array: {arr}")
