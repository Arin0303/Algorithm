import sys
import bisect

input = sys.stdin.readline

# 1. 데이터 입력받기
N = int(input())
# N개의 숫자를 리스트 A에 저장
A = list(map(int, input().split()))

M = int(input())
# 찾아야 할 M개의 숫자들을 리스트 targets에 저장
targets = list(map(int, input().split()))

# 2. 이진 탐색을 위한 정렬
A.sort()

# 3. 각 target에 대해 이진 탐색 수행
for target in targets:
    # bisect_left는 target이 리스트 A에 삽입될 왼쪽 인덱스를 반환
    index = bisect.bisect_left(A, target)
    
    # 찾은 인덱스가 리스트 범위 내에 있고, 해당 위치의 값이 target과 일치하는지 확인
    if index < N and A[index] == target:
        print(1)  # 존재하면 1 출력
    else:
        print(0)  # 존재하지 않으면 0 출력