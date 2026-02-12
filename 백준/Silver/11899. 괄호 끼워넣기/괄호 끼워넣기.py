from collections import deque
arr = input()
close = 0
open = 0
for i in range(len(arr)):
    if (arr[i] == '('):
        open += 1
    else:
        close += 1
        if(open > 0):
            open -= 1
            close -= 1
print(open + close)