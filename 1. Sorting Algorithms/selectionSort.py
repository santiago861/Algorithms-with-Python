# ---------------------------------------------------------------------------------------------------------------------
# Selection Sort implementation
# optimal only on relative small datasets, no more than 10,000 elements
# it runs in O(n^2)

def selectionSort(arr):
    print('---------------------------------------------- Selection Sort ----------------------------------------------')
    for i in range (0, len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        print(arr, arr[i], arr[minIndex]) # -- uncomment to see changes
        if minIndex != i:
            temp = arr[minIndex]
            arr[minIndex] = arr[i]
            arr[i] = temp
    return arr