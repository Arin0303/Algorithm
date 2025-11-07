n, s = map(int, input().split())
arr = list(map(int, input().split()))

count = 0  # 합이 s가 되는 부분수열 개수

def backtrack(index, current_sum):
    global count

    # 모든 원소를 다 봤으면 종료
    if index == n:
        if current_sum == s:
            count += 1
        return

    # 현재 원소를 선택하는 경우
    backtrack(index + 1, current_sum + arr[index])
    
    # 현재 원소를 선택하지 않는 경우
    backtrack(index + 1, current_sum)

# 시작: 인덱스 0, 현재 합 0
backtrack(0, 0)

# 공집합(아무것도 선택 안한 경우) 제외
if s == 0:
    count -= 1

print(count)
