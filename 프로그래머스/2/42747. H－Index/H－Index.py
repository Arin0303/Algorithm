"""
[3, 0, 6, 1, 5]	
논문의 수: len(citations) = 5
원소: 논문 인용 횟수
논문 3(h)편(3,6,5) -> 3(h)번 이상 인용
나머지 논문(0,1) -> 3(h)번 이하 인용
return 3

100 100 100 -> 100 (citations[i]) > 3 (n - i) -> h=3  

1 2 3 4 5 ->   3 (citations[i]) == 3 (n - i) -> h=3
"""


def solution(citations):
    h = 0
    
    citations.sort()
    
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i: # 현재 논문 인용 횟수 >= 남은 논문 개수
            h = n - i
            return h
    return 0







