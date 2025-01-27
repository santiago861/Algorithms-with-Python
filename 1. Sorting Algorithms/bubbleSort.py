# ---------------------------------------------------------------------------------------------------------------------
# Bubble Sort implementation
# to better understand this algorithm think about de i and j from the loops as the times it will run the instructions

def bubbleSort(arr):
    print('---------------------------------------------- Bubble Sort ----------------------------------------------')
    for i in range(0, len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            print(arr, arr[j], arr[j + 1]) # uncomment to see changes
            if arr[j + 1] < arr[j]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        print(arr) # uncomment to see changes
    return arr