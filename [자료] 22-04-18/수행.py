list1=[]
list2=[]
list3=[]

import random as r

for i in range(4):
    list1.append(r.randint(1,51))
    list2.append(r.randint(1,51))

list3.extend(list1)
list3.extend(list2)

print("list3의 길이는 %d 입니다" % len(list3))

list3.sort()
print("제일 큰 값은 %d 입니다" % list3[-1])
list3.reverse()
print("제일 작은 값은 %d 입니다" % list3[-1])

print("제일 작은 값 %d 를 삭제했습니다" % list3.pop(-1))

list3.insert(0,list3[0]+10)

list3.sort()
list3.reverse()
print(list3)