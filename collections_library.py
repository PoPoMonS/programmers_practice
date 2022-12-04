from collections import Counter

list = ["red", "blue", "blue", "green", "red", "blue"]

# 등장 횟수 세기

counter = Counter(list)

print(counter['blue'])
print(counter['green'])
print(dict(counter))

