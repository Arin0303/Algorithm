word = input().upper()

freq = {}

for ch in word:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_value = 0 # 나온 빈도수(value)
max_char = '' # 알파벳(key)
duplicate = False

for key in freq:
    if freq[key] > max_value:
        max_value = freq[key]
        max_char = key
        duplicate = False
    elif freq[key] == max_value:
        duplicate = True

if duplicate:
    print("?")
else:
    print(max_char)

