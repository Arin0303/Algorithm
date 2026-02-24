"""
참여자: participant
완주자: completion

완주x 선수 이름(1명) return 

"""
def solution(participant, completion):
    hash = {}
    for p in participant:
        hash[p] = hash.get(p,0) + 1 # 참여자 딕셔너리 세팅
    for c in completion:
        hash[c] -= 1
    
    for p in participant:
        if(hash[p] > 0):
            answer = p
            break
    return answer
