def szczyt(X,Y):
    n=len(X)
    A = []
    first = True
    for i,j in zip(X,Y):
        if first:
            A.append(i)
            A.append(j)
            first = False
        else:
            if (A[0]/A[1]) > (i/j):
                A[0], A[1] = i,j
    return A[0],A[1]


print(szczyt([1,3,2,-2],[3,4,1,2]))

def szczyty(X,Y):
    n=len(X)
    A = []
    first = True
    for i,j in range(len(n)):
        if first:
            A.append(X[i])
            A.append(Y[j])
            first = False
        else:
            if (A[0]/A[1]) > (X[i]/Y[i]):
                A[0], A[1] = X[i],Y[i]
    return A[0],A[1]

print(szczyt([1,3,2,-2],[3,4,1,2]))