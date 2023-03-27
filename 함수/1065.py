# 구글 검색을 해보면 다들 자릿수를 지정해서 99까지는 count하는 방식에 등차수열의 자릿수를 nums[0] - nums[1] == nums[1] - nums[2]로
# 체크를 하는 방법으로 다들 하였더라. 일단은 나도 1일 1커밋을 해야하기에 고민하다가 올리기는 하지만
# 만약에.. 입력 부분의 '첫째 줄에 1000보다 작은 자연수 N이 주어진다'의 요구조건이 변경된다면??
# 흠.. 좀 더 유연한? 코드를 짜야 할 것 같다.

# 한수

# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 예제 입력 - 110
# 예제 출력 - 99

def check_hansu(strNumber, strNumberLength):

    hansu = 0

    for n in range(1, int(strNumber) + 1):

        # 1부터 99까지는 모두 한수
        if n <= 99:
            hansu += 1

        else:
            # 숫자를 자릿수대로 분리
            nums = list(map(int, str(n)))
            # 등차수열 확인 -> 1000보다 작기때문에 가능한 조건..
            if nums[0] - nums[1] == nums[1] - nums[2]:
                hansu += 1

    return hansu


# 입력받은 자연수
number = input()
# 자연수의 자리수
numberLength = len(number)

# 입력받은 자연수, 자연수의 자리수를 파라미터로 넘겨줌
print(check_hansu(number, numberLength))
