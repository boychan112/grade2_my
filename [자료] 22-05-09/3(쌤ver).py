def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1,len(A)):
        if max<A[i] : max=A[i]
        if min>A[i] : min=A[i]
    return min,max

data=input("숫자를 입력하세요: ").split()
x,y=find_min_max(data)
print("(min,max) = ",(x,y))