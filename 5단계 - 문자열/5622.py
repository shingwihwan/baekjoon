# 다이얼

word = input()

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

total = 0

for i in word:
    for alphabet in dial:
        if alphabet.find(i) != -1:
            total += (dial.index(alphabet) + 3)

print(total)