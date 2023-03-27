# 별 찍기 - 7

star = int(input())

max_star_count = 2 * star - 1

total = ''

for i in range(1, max_star_count + 1, 2):
    space = int(((max_star_count - i) / 2))
    if i != max_star_count:
        print((space * " ") + i * '*')

for j in range(max_star_count, 0, -2):
    space = int((max_star_count - j) / 2)
    print((space * " ") +j * '*')
