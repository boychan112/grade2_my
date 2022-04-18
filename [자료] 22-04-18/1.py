odd=[1,3,[5,7,9],10,11,12]
print(odd[2][1])

array=[[1,3,5,7],[2,4,6,8]]
print(array[0][1]*array[1][1])

a=[1,2,3,4,5,6,7,8,9,10]
print(a[4:10])
print(a[0:5])
print(a[:5])
print(a[5:])

print(len(a)) #길이 알려주는 함수
a.append(11) #a배열 맨 뒤에 11 추가
print(a)

b=['a','b','c','d','e']
print(a+b)

a.extend(b) #a에 b를 추가 넣어버렸!!!!
print(a)

c=[54,543,35,351,414]
c.sort() #오름차순 정렬 #반대로 뒤집기 reverse   
print(c)

a.insert(0,12) #a의 0번쨰 위치에 12 삽입
print(a)

a.remove(1) #1이라는 값 삭제
print(a)

a.pop(0) #0번째 값 삭제
print(a)

print(a.count(6)) #6이 몇개 들어있는지