import sys
input = sys.stdin.readline

n = int(input()) # 시험장 개수 (1~)


input_string = input() # 문자열
a = list(map(int, input_string.split())) # 문자열 리스트 -> int로 변환(각 시험장의 응시자 수)

b, c = map(int, input().split())

result = 0

for i in range(n):
    if(a[i] > 0): # 응시자가 존재하면 
        a[i] = a[i] - b # 총감독관 한 명 먼저 배치
        result = result + 1 # 감독관 수 1 증가
    
    if(a[i] > 0):    
        quote = a[i] // c
        result = result + quote 
        #print("몫: result = ", result)
        if((a[i] % c) != 0):
            result = result + 1
            #print("나머지 추가: result = ", result)
    

print(result)