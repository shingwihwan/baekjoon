# 단어 공부

word = input()
lower_word = word.lower()

sett = {}
key = ""
value = 0

# 딕셔너리에 키, 값으로 넣어주기
for i in lower_word:
    if sett.get(i):
        sett.update({i: sett.get(i) + 1})
        continue
    sett.update({i: 1})

# 딕셔너리 최고 카운트 가려내기
for j in sett:
    if value < sett.get(j):
        key = j
        value = sett.get(j)
    elif value == sett.get(j):
        key = "?"

print(key.upper())

