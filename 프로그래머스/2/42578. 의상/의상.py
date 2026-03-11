"""
{
    "headgear": 2,
    "eyewear": 1,
}

2+1 = 3
total_kind = 2
2x1=2
-> 
"""

def solution(clothes):
    closet = {}
    total_kind = 0
    each_count = 0
    comb_count = 1
    result = 1
    
    for name, kind in clothes: 
        if kind in closet:
            closet[kind] += 1
            each_count += 1 # 개별 카운트 
        else:
            closet[kind] = 1
            total_kind += 1 # kind 개수(조합 계산시 필요)
            each_count += 1 # 개별 카운트 

    # 조합 계산
    for c in closet.values():
        c = c + 1 
        result *= c
    result = result - 1 # 하나도 입지 않는 경우의 수 제외
    return result
    