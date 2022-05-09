def find_max(A) :
    max=A[0]
    for i in range(1,len(A)):
        if max < A[i]:
            max = A[i]
    return max

data=[1,23,14,125,125,1,124,124,125,16,4,7,5474,5]
print("max = ", find_max(data))