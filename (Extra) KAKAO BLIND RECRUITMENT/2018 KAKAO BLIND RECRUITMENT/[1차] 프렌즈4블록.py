# Solved. But not make up yet.


def solution(m, n, board):
    answer = 0

    boardT = [ "" for x in range(n) ]
    for j in range(n):
        for i in range(m):
            boardT[j] += board[i][j]

    while True:
        pool = set()

        for x in range(m-1):  # 0 ~ m-1까지 탐색 (행)
            for y in range(n-1):  # 0 ~ n-1까지 탐색 (열)
                target = boardT[y][x]  # boardT는 열, 행

                if target == '0':
                    continue

                if target != boardT[y][x+1]:  # 오른쪽
                    continue
                elif target != boardT[y+1][x]:  # 아래
                    continue
                elif target != boardT[y+1][x+1]:  # 대각선
                    continue
                else:
                    pool.add((y, x))
                    pool.add((y, x+1))
                    pool.add((y+1, x))
                    pool.add((y+1, x+1))

        thisRoundCnt = len(pool)
        for p in pool:
            Y = p[0]
            X = p[1]
            boardT[Y] = boardT[Y][:X] + '0' + boardT[Y][X+1:]

        # print(boardT)

        for j in range(n):
            boardT[j] = boardT[j].replace('0', '', -1)

            if len(boardT[j]) != m:
                boardT[j] = '0' * (m - len(boardT[j])) + boardT[j]

        # print(boardT)


        if thisRoundCnt != 0:
            answer += thisRoundCnt
            thisRoundCnt = 0
        else:
            break

    return answer


if __name__ == '__main__':
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))


"""
board 탐색을 반복하면서, 한 싸이클에 없앨 수 있는 블록 찾아서 없애고
다음 사이클 탐색하고를 반복! -> 한사이클에서 없앨 수 있는 블록이 없다면 BREAK

(0,0)에서 (m-1,n-1)까지 탐색
탐색하는 블록에 오른쪽, 아래, 대각선 오른쪽 아래가 전부 같은 글자인지 판단!
(만약 탐색 대상중에 다른글자가 나오면 패스)
    모두 같은 글자면, 해당 좌표값들 set에 저장 (바로 0으로 치환해버리면, 중복될 경우 찾을 수가 없음)
    아니라면, 패스

한 사이클을 돈 후, 해당 좌표값들에 해당하는 갯수만큼 카운트(중복 제외!)

사라지는 좌표값들 전부 다른 글자로 치환 ('0' 같은거로)
한 열씩 체크하면서 '0'을 제외한 글자들로 다시 열 만듬
ex. T T 0 C F 0 M  ->  T T C F M 0 0 
    (새롭게 리스트 만들고, 뒤에 m개가 되도록 0 채워줌)
    새로 만든 줄로 대체 (하나씩 원소를 대체해주는 방식이 나을 거 같음)

빈 공간은 '0' 처리 (탐색때도 '0'은 처리 안하도록!)

위 반복하면서 한 사이클에 지워지는게 없으면 끝!


while True:
    thisRoundCnt = 0
    
    ...
    
    if thisRoundCnt:
        answer += thisRoundCnt
        thisRoundCnt = 0
    else:
        break

"""