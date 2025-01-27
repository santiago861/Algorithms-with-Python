# ---------------------------------------------------------------------------------------------------------------------
# Insertion Sort implementation
# optimal only on relative small datasets, no more than 10,000 elements
# it runs in O(n^2)
# the expensive operation is swaping value, each time we make a swap, three operation take place

def insertionSort(arr):
    print('---------------------------------------------- Insertion Sort ----------------------------------------------')
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > currentVal:
            arr[j + 1] = arr[j]
            j -= 1
        print(arr, currentVal) # -- uncomment to see changes
        arr[j + 1] = currentVal
    return arr