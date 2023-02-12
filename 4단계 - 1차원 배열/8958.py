# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다.
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
# 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

# 예제 입력 - 5
#            OOXXOXXOOO
#            OOXXOOXXOO
#            OXOXOXOXOXOXOX
#            OOOOOOOOOO
#            OOOOXOOOOXOOOOX

# 예제 출력 - 10
#            9
#            7
#            55
#            30

# 테스트 케이스 개수
case_count = input()

# 입력받은 OX정보를 리스트에 담기위한 변수
ox_list = []

# 테스트 케이스 개수만큼 OX를 입력받음.
# 입력 받은 후 ox_list에 append
for i in range(int(case_count)):
    ox = input()
    ox_list.append(ox)


def count_o(str):
    num1 = 0
    num2 = 0
    before_o = False

    # 첫 시작이 O면 1을 대입해주고 before_o 변수를 True
    if str[0] == "O":
        num1 = 1
        num2 = 1
        before_o = True

    for i in range(1, len(str)):
        if str[i] == "X":
            before_o = False
            num1 = 0
        if str[i] == "O":
            if before_o == True:
                num1 += 1
                num2 += num1
            else:
                before_o = True
                num1 += 1
                num2 += num1

    return num2


for i in range(len(ox_list)):
    print(count_o(ox_list[i]))
