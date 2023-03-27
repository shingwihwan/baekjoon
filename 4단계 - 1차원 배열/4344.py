# 평균은 넘겠지

# 문제
# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
# 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

# 예제 입력 - 5
#            5 50 50 70 80 100
#            7 100 95 90 80 70 60 50
#            3 70 90 80
#            3 70 90 81
#            9 100 99 98 97 96 95 94 93 91

# 예제 출력 - 40.000%
#            57.143%
#            33.333%
#            66.667%
#            55.556%

# 케이스 개수
case_count = input()

case_list = []

# 학생의 수 + N 명의 점수 입력 후 list에 append
for i in range(int(case_count)):
    case_list.append(input())


# 평균을 넘는 학생수 비율을 출력하는 함수
def point_average(student_count, input_list):

    # 점수 합산
    point = 0
    # 평균을 넘는 학생수 카운트
    ave_count = 0

    # 점수 합산 for문
    for i in range(1, len(input_list)):
        point += int(input_list[i])

    # 점수 합산 / 학생 수 = 평균 점수
    ave_point = point / student_count

    # 평균 점수를 넘는 카운트 세기
    for i in range(1, len(input_list)):
        if int(input_list[i]) > ave_point:
            ave_count += 1

    # 평균 점수를 넘는 비율 계산
    output = (ave_count / student_count) * 100

    return print(format(output, ".3f") + "%")


# 케이스 개수만큼 for문을 돌리기
for i in range(len(case_list)):

    # 빈 문자열로 자른 후 학생수와 점수 list에 다시 담기
    input_list = case_list[i].split(" ")

    # 학생 수
    student_count = int(input_list[0])

    # 평균 내는 함수
    point_average(student_count, input_list)
