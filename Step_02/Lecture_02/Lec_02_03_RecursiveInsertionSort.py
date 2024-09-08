def recursive_insertion_sort(arr, n=None):
    if n is None:
        n = len(arr)

    if n <= 1:
        return

    recursive_insertion_sort(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last


arr1 = [12, 11, 13, 5, 6]
recursive_insertion_sort(arr1)
print("Sorted array:", arr1)

arr2 = [4, 3, 2, 10, 12, 1, 5, 6]
recursive_insertion_sort(arr2)
print("Sorted array:", arr2)
