def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        zmienna = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                zmienna = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if zmienna == False:
            break
arr = [1,3,8,2,39,4]
arr2 = ["a","x","A","p","X","9"]
bubbleSort(arr)
bubbleSort(arr2)

print(bubbleSort(arr))
print(arr)
print(arr2)