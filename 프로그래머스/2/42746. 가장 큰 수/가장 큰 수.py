"""
key: 앞 뒤 문자열 비교 -> 함수
"""

from functools import cmp_to_key

def solution(numbers):
    
    def compare(a,b): # a = 6 b = 10
        if a + b > b + a:  # 610 106
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
        
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))
    answer = ''.join(numbers) # 문자열
    
    if answer[0] == '0':
        return '0'
    return answer
