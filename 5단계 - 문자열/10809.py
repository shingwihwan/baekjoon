lower_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]

a = input()

for i in lower_alphabet:  # a
    loc = lower_alphabet.index(i)  # 0
    for j in a:  # b
        a_index = a.index(j)  # 0
        if i == j:
            lower_alphabet[loc] = a_index
            break
        else:
            lower_alphabet[loc] = -1

for j in range(len(lower_alphabet)):
    print(lower_alphabet[j], end=" ")

# 아래 풀이는 다른 사람 풀이

word = input()
alphabet = list(range(97, 123))  # 아스키 코드 숫자 범위

for x in alphabet:
    print(word.find(chr(x)))
