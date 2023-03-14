# 문자열 반복

test_count = int(input())

result = ""
for _ in range(test_count):
    count, word = input().split(" ")

    for i in word:
        for j in range(int(count)):
            result += i

    result += " "

print(result)
