n = int(input())
stack = []
for i in range(n): # n번 반복 
    token = int(input()) # 정수 입력 받기
    if(token == 0): # 0이 입력되면 가장 최근에 들어온 수 제거
        stack.pop()
    else:
        stack.append(token) # 0이 아니면 스택에 추가

print(sum(stack)) # sum(): 리스트의 모든 원소의 합을 반환
