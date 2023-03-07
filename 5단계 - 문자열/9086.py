case_count = int(input())

result = []

for i in range(case_count):
    word = input()

    imp = ""

    # 단어가 한개인 경우
    if len(word) < 2:
        imp = word[0] + word[0]

    imp = word[0] + word[len(word) - 1]

    result.append(imp)

for j in range(case_count):
    print(result[j])
