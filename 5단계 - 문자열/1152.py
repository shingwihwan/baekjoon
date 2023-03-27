# 단어의 개수

word = input().split(" ")

count = 0

for i in word:
    if i != "":
        count += 1

print(count)