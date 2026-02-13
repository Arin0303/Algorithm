# 문자열을 리스트로 입력받기
a, b = input().split()
a = list(a)
b = list(b)

# 역순 정렬
a.reverse()
b.reverse()

# 리스트 -> 문자열
a = ''.join(a)
b = ''.join(b)

print(max(a,b))