def solution(array, commands):
    answer = []
    for i,j,k in commands:
        sorted_arr = array[i-1:j]
        sorted_arr.sort()
        key = sorted_arr[k-1]
        answer.append(key)
    return answer