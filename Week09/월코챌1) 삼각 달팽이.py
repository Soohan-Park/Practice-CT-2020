# Solved

def solution(n):
    answer = []
    board = []

    for i in range(n):
        row = [ None for _ in range(i+1) ]
        board.append(row)

    r, v = 0, 0
    cur = 1
    while True:
        while True:  # 다운
            board[r][v] = cur

            if r == n-1 or board[r+1][v] is not None:
                v += 1
                cur += 1
                break

            r += 1
            cur += 1

        if isEnd(board) : break

        while True:  # 라이트
            board[r][v] = cur

            if v == n-1 or board[r][v+1] is not None:
                r -= 1
                v -= 1
                cur += 1
                break

            v += 1
            cur += 1

        if isEnd(board): break

        while True:  # 업
            board[r][v] = cur

            if board[r-1][v-1] is not None:
                r += 1
                cur += 1
                break

            r -= 1
            v -= 1
            cur += 1

        if isEnd(board) : break

    for b in board:
        answer.extend(b)

    return answer


def isEnd(_board):
    flag = True
    for b in _board:
        if None in b:
            flag = False
            break

    return flag


if __name__ == '__main__':
    print(solution(4))
    print(solution(5))
    print(solution(6))


"""
n 만큼 전체 갯수를 만듬 (sigma n)
피라미드에 맞게 None으로 채워진 board 만듬

r, v : 행, 열
다운 : r + 1, v
라이트 : r, v + 1
업 : r - 1, v

위 모두, 진행방향에서 앞에 것이 있다면 다음 방향으로 넘어간다.

while board에 None이 없을 때까지
    while 다운:
        r 이 n-1이거나, 다음에 값이 None이 아닐때까지 반복
    while 라이트:
        v가 n-1이거나, 다음에 값이 None이 아닐때까지 반복
    while 업:
        다음의 값이 None이 아닐 때까지 반복 (제일 위에는 이미 1이 채워져 있음)

board 순서대로 합쳐서 Return
"""