def Insert_sort(A):
    n = len(A)
    for i in range(1,n):
        aktualny = A[i]
        inny = i - 1
        while inny >= 0 and aktualny < A[inny]:
            A[inny + 1] = A[inny]
            inny = inny - 1
        A[inny + 1] = aktualny 

arr = [64, 34, 25, 12, 22, 11, 90]
Insert_sort(arr)

print(arr)