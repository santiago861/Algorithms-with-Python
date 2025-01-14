arr = [2, 234, 12, 64, 83, 23, 47, 982, 1, 3, 4, 2, 12, 54, 334, 64, 865, 32]
arr2 = [1, 7, 8, 2, 3]
arr3 = [2, 234, 12, 1, 32]

# ---------------------------------------------------------------------------------------------------------------------
# Insertion Sort implementation
# optimal only on relative small datasets, no more than 10,000 elements
# it runs in O(n^2)
# the expensive operation is swaping value, each time we make a swap, three operation take place

def insertionSort(arr):
    print('----------------------------------------------  Insertion Sort ---------------------------------------------- ')
    for i in range(1, len(arr)):
        currentVal = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > currentVal:
            arr[j + 1] = arr[j]
            j -= 1
        print(arr, currentVal) # -- uncomment to see changes
        arr[j + 1] = currentVal
    return arr
# ---------------------------------------------------------------------------------------------------------------------
# Selection Sort implementation
# optimal only on relative small datasets, no more than 10,000 elements
# it runs in O(n^2)

def selectionSort(arr):
    print('---------------------------------------------- Selection Sort ---------------------------------------------- ')
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
# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort implementation
# to better understand this algorithm think about de i and j from the loops as the times it will run the instructions

def bubbleSort(arr):
    print('----------------------------------------------  Bubble Sort ---------------------------------------------- ')
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            print(arr, arr[j], arr[j + 1]) # uncomment to see changes
            if arr[j + 1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print(arr) # uncomment to see changes
    return arr
# ---------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    # print(insertionSort(arr2))
    # print(selectionSort(arr2))
    print(bubbleSort(arr2))