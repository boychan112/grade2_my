stack=[]

def isEmpty(): #stack이 비어있는지 확인
    #비어있으면 true, 비어있지 않으면 false 반환
    return len(stack)==0
def push(item):
    #매개변수 item을 stack의 마지막 index에 저장
    stack.append(item)
def pop():
    #최근에 들어온 값(마지막 인덱스 값) 반환하고 삭제
    if not isEmpty():
        return stack.pop(-1)
def peek():
    #최근에 들어온 값(마지막 인덱스 값) 반환
    if not isEmpty():
        return stack[-1]
def size():
    #stack에 들어있는 항목의 갯수 반환
    return len(stack)
def clear(): #stack을 공백으로 전환
    global stack
    stack=[]

for i in range(1,6): #1,2,3,4,5 push 5번
    push(i)

print("push 5회 실시", stack)
#stack에 들어 있는 값 확인
print("pop()-> ", pop())
#pop실행 어떤 값이 반환되고 삭제되었나
print("pop()-> ", pop())
print("pop() 2회 : -> ", stack)
#pop을 2번 실시하고 stack에 들어 있는 값 출력