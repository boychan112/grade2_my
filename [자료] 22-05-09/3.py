def find_min_max(A):
    min=A[0]
    max=A[0]
    for i in range(1,len(A)):
        if max<A[i] : max=A[i]
        if min>A[i] : min=A[i]
    return min,max

data=[]
for a in range(10):
    b=int(input("숫자 10개 입력하세요 : "))
    data.append(b)
x,y=find_min_max(data)
print("(min,max) = ",(x,y))