# 공넣기

# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다.
# 또, 1번부터 N번까지 번호가 적혀있는 공을 매우 많이 가지고 있다.
# 가장 처음 바구니에는 공이 들어있지 않으며, 바구니에는 공을 1개만 넣을 수 있다.
# 도현이는 앞으로 M번 공을 넣으려고 한다.
# 도현이는 한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
# 만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
# 공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.
# 둘째 줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다. 각 방법은 세 정수 i j k로 이루어져 있으며,
# i번 바구니부터 j번 바구니까지에 k번 번호가 적혀져 있는 공을 넣는다는 뜻이다.
# 예를 들어, 2 5 6은 2번 바구니부터 5번 바구니까지에 6번 공을 넣는다는 뜻이다. (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
# 도현이는 입력으로 주어진 순서대로 공을 넣는다.

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다. 공이 들어있지 않은 바구니는 0을 출력한다.

# 예제 입력 1 -  5 4            예제 출력 1 - 1 2 1 1 0
#               1 2 3
#               3 4 4
#               1 4 1
#               2 2 2

nm = input()
nm_split = nm.split(" ")

n = nm_split[0]
m = nm_split[1]

n_list = [0 for i in range(int(n))]

for i in range(int(m)):
    abc = input()
    abc_slpit = abc.split(" ")

    a = int(abc_slpit[0]) - 1
    b = int(abc_slpit[1]) - 1

    c = abc_slpit[2]

    if b - a > 1:
        for j in range(b + 1):
            n_list[j] = c
    elif b - a == 1:
        n_list[a] = c
        n_list[b] = c
    elif b - a == 0:
        n_list[b] = c

for k in range(len(n_list)):
    print(n_list[k], end=' ')


# 다른사람 풀이
N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n] = k

for i in range(1, N+1):
    print(basket[i], end=' ')
