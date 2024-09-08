def merge(arr, l, m, r):
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)

        merge(arr, l, m, r)


arr1 = [4, 1, 3, 9, 7]
mergeSort(arr1, 0, len(arr1) - 1)
print("Sorted array:", arr1)

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(arr2, 0, len(arr2) - 1)
print("Sorted array:", arr2)
