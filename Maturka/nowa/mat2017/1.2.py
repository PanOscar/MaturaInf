def prostokat(A, p):
    n = len(A)
    maks1 = 0
    maks2 = 0
    for i in range(n):
        if(A[i]%p!=0):
            if A[i] > maks1:
                maks2 = maks1
                maks1 = A[i]
            elif A[i] > maks2:
                maks2 = A[i]
    return maks1 * maks2

print(prostokat([7,5,11,33],3))