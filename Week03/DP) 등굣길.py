# Solved with Solution.
# https://codedrive.tistory.com/57
# Comment: 최단거리 구하는 거( [x-1, y] + [x, y-1] )로 하면 됨.. 효율성이 해결되었다.
#          tempPool에 append 하는 것에서 효율성이 많이 떨어졌던 것 같다.


def solution(m, n, puddles):
    answers = [ [0] * (m+1) for i in range(n + 1)]
    answers[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i==1 and j==1:
                continue
            if [j, i] in puddles:
                answers[i][j]=0
            else:
                answers[i][j] = answers[i-1][j] + answers[i][j-1]

    return answers[n][m] % 1000000007


"""
def solution(m, n, puddles):
    pool = [ [1,1] ]

    while True:
        tempPool = []
        for target in pool:
            #target = pool.pop()  || pop(0)를 쓰면 더 안좋은 효율성이 나온다.
            x = target[0]
            y = target[1]

            rightTile = [x + 1, y]
            downTile = [x, y + 1]

            if rightTile not in puddles: tempPool.append(rightTile)
            if downTile not in puddles: tempPool.append(downTile)

        pool = tempPool
        if [m, n] in tempPool: break

    return pool.count([m,n]) % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))
"""
