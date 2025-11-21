import sys
input = sys.stdin.readline
from collections import deque # 방문 할 컴퓨터를 저장할 덱

comp_num = int(input()) # 컴퓨터의 수(1 ~ 100)
pair_num = int(input()) # 연결된 컴퓨터 쌍의 수

# 그래프 초기화
pair_comp = {i: [] for i in range(1, comp_num + 1)}


# 연결 정보 저장
for _ in range(pair_num):
    comp1, comp2 = map(int, input().split())
    pair_comp[comp1].append(comp2)
    pair_comp[comp2].append(comp1)

def dfs(pair_comp, start_comp):
    infected_comp = [] # 감염된 컴퓨터들을 저장할 리스트
    soon_infected_comp = deque() # 감염될 컴퓨터들을 저장할 스택

    soon_infected_comp.append(start_comp) 

    while soon_infected_comp:
        comp = soon_infected_comp.pop()

        # 감염되지 않았으면
        if comp not in infected_comp:
            # 감염된 리스트에 추가
            infected_comp.append(comp)
            soon_infected_comp.extend(pair_comp[comp]) # 연결된 컴퓨터를 곧 감염될 스택에 추가

    # 1번을 제외한 감염된 수
    return len(infected_comp) -1 

# 1번 컴퓨터가 바이러스에 걸렸을 때, 1번을 통해 전파되는 컴퓨터의 수
print(dfs(pair_comp, 1))