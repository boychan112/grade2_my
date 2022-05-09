def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1,len(A)):
        if max<A[i] : max=A[i]
        if min>A[i] : min=A[i]
    return min,max

data = [1,123,145,15,125,15,161,2,67,54,56,82]
x,y=find_min_max(data)
print("(min,max) = ",(x,y))