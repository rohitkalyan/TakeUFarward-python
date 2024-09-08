def recursive_bubble_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n == 1:
        return

    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    recursive_bubble_sort(arr, n - 1)


arr1 = [64, 34, 25, 12, 22, 11, 90]
recursive_bubble_sort(arr1)
print("Sorted array:", arr1)

arr2 = [5, 1, 4, 2, 8]
recursive_bubble_sort(arr2)
print("Sorted array:", arr2)
