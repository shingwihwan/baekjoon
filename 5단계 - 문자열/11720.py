# 숫자의 합

len_num = int(input())
num = input()
result = 0

for i in range(len_num):
    result += int(num[i])

print(result)
