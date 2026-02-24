"""
N -> N/2마리 가져가기

[3,1,2,3]	2
2개 뽑아서 최대 2종류

[3,3,3,2,2,4]	3
3개 뽑아서 최대 2종류

[3,3,3,2,2,2]	2
3개 뽑아서 최대 2종류
"""

def solution(nums):
    result = min(len(set(nums)), len(nums)/2)
    return result