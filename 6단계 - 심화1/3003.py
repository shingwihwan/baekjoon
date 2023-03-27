# 킹, 퀸, 룩, 비숍, 나이트, 폰

chess = ['1', '1', '2', '2', '2', '8']
# 0 1 2 2 2 7
# 2 1 2 1 2 1
data_list = input().split(' ')

result_str = ''

for i in range(6):
    chess_data = int(chess[i])
    list_data = int(data_list[i])

    if chess_data > list_data:
        data = chess_data - list_data
        result_str += str(data)
        result_str += ' '
    elif chess_data < list_data:
        data = chess_data - list_data
        result_str += str(data)
        result_str += ' '
    else:
        result_str += '0'
        result_str += ' '

print(result_str)

# 다른 분들 코드

chess1 = [1, 1, 2, 2, 2, 8]

a = list(map(int, input().split()))

for i in range(6):
    print(chess1[i] - a[i], end=' ')
