# 상수

nums = input().split(" ")

num1 = nums[0]
num2 = nums[1]

num3 = ""
num4 = ""

for i in num1[::-1]:
    num3 += i

for j in num2[::-1]:
    num4 += j

if int(num3) > int(num4):
    print(num3)
else:
    print(num4)
