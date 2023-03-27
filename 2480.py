# 주사위 세개

dice = input().split(" ")

one = dice[0]
two = dice[1]
three = dice[2]

if one == two == three:
    print(10000 + (int(one) * 1000))
elif one == two:
    print(1000 + (int(one) * 100))
elif one == three:
    print(1000 + (int(one) * 100))
elif two == three:
    print(1000 + (int(two) * 100))
else:
    max = 0
    for i in dice:
        if int(i) > max:
            max = int(i)
    print(max * 100)
