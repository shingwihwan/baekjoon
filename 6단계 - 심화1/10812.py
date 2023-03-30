# 바구니 순서 바꾸기

nm = input().split(" ")

n = nm[0]
m = nm[1]

n_list = [int(i + 1) for i in range(int(n))]


def change_sequence(numbers):
    begin = int(numbers[0])
    end = int(numbers[1])
    mid = int(numbers[2])

    tmp_list = []

    # 리스트에서 숫자 뽑아서 임시 리스트에 담기
    for i in range((end - mid) + 1):
        tmp_list.append(n_list.pop(mid - 1))

    # 임시 리스트에 담은 숫자를 리스트에 넣기
    for j in range(len(tmp_list)):
        n_list.insert(begin - 1, tmp_list[j])
        begin += 1


for i in range(int(m)):
    abc = input().split(" ")
    change_sequence(abc)

print(*n_list)

# 다른 사람 풀이

N, M = map(int, input().split())
result = [i for i in range(1, N + 1)]
for _ in range(M):
    i, j, k = map(int, input().split())
    result = result[:i - 1] + result[k - 1:j] + result[i - 1:k - 1] + result[j:]
print(result)
