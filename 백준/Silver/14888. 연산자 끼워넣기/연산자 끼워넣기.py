import sys
input = sys.stdin.readline

N = int(input()) # 피연산자 개수
num = list(map(int, input().split())) # 피연산자
op = list(map(int, input().split())) # 연산자(+, -, *, //)

maximum = -1e9 # 가장 작은 값 대입
minimum = 1e9 # 가장 큰 값 대입

# depth: 사용한 숫자의 개수
# total: 누적 계산 값 
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum # 전역변수 수정 권한
    
    if depth == N: # 모든 피연산자를 다 사용했을 때
        # maximum과 minimum은 재귀함수의 지역 변수가 아니기 때문에 재귀호출이 끝났더라도 값은 유지되므로 각 경우마다 max, min 갱신이 가능하다.
        maximum = max(total, maximum) 
        minimum = min(total, minimum) 
        return 
    
    
    if plus: # plus가 존재하면 첫번째 간격은 +로하고 이후 간격들 채우기
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide) # 재귀호출 시작

    if minus: # minus가 존재하면 첫번째 간격은 -로 하고 이후 간격들 채우기
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)

    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)

    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3]) # depth = 1: 숫자 1개 사용
                                           # total = num[0]: 첫 번쨰 숫자 total에 대입하여 이후에 연산자로 갱신할거임
print(maximum)
print(minimum)
        

