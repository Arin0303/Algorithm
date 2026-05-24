"""
key: 앞 뒤 문자열 비교 -> 함수
"""

from functools import cmp_to_key

def solution(numbers):
    def compare(a,b):
        if a + b > b + a:
            return -1
        elif a + b < b + a: 
            return 1
        else:
            return 0
    
    numbers = list(map(str, numbers)) # 문자열 리스트
    
    numbers.sort(key=cmp_to_key(compare))
    
    answer = ''.join(numbers) # 이어붙이기    
                   
    if answer[0] == '0':
        return '0'
    
    return answer
