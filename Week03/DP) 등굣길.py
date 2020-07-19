# Test Case 8, 10  시간초과 -> 효율성 재고 필요.


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
        if [m, n] in tempPool:
            break

    return pool.count([m,n]) % 1000000007


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))
