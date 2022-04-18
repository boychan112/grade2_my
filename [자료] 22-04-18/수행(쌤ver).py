import random as rd

# a=rd.randint(0,101) #1~100 까지 랜덤한 정수 1개
# b=rd.randrange(0,101,2)
# print(a);print(b)

list1=[]
list2=[]
for _ in range(4): #random 정수 list에 추가
    list1.append(rd.randint(1,51))
    list2.append(rd.randint(1,51))
   
#print(list1)
#print(list2)
list3=[]
list3.extend(list1)#list3에 list1,2 합치기
list3.extend(list2)
list3
print("list3의 길이는: %d, list3은: %s" % (len(list3),list3)) #list3의 길이와 요소 출력
list3.sort() #list3정렬
print(list3)
print("list3에서 가장 작은값:%d , 가장 큰 값:%d" %(list3[0],list3[-1]))
print("가장 작은 값인 %d 삭제" % list3.pop(0))
print("삭제 후 결과:",list3)#삭제 후 결과
list3.insert(0,list3[-1]+10)
#0번쨰 index에 가장큰 값+10 을 삽입 가장큰 값은 마지막 인덱스(음수표현으로 -1)
print(list3)
list3.sort() #정렬시키고
list3.reverse()#역순으로 바꾸면 내림차순 정렬됨
print(list3)