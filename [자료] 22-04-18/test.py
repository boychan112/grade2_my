list1 = [] #빈 리스트 선언
list2 = []

list1.append(12) #list1에 값 추가
list1.append(54)
list1.append(36)
list1.append(7)
list2.append(12) 
list2.append(4)
list2.append(3)
list2.append(12)

list1.extend(list2)

list1.insert(0,100)
list1.insert(5,250)
print(list1)

print("삭제된 원소는 : %d" % list1.pop(-1))
print("삭제된 원소는 : %d" % list1.pop(-1))
print(len(list1))
print(list1)

list1.reverse()
print(list1)

print(list1.count(12))