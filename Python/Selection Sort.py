def selection_sort(arr):
    for j in range(len(arr) - 1):
        min_index = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[min_index]:
                min_index = i
        arr[j], arr[min_index] = arr[min_index], arr[j]
        print(f"After iteration {j + 1}: {arr}")


arr = [64, 25, 12, 22, 11]
print(f"Original array: {arr}")
selection_sort(arr)
print(f"Sorted array: {arr}")
