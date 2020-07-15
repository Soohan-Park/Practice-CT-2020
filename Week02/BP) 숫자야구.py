# 테스트 케이스 6, 7, 10이 계속 틀림...

def solution(baseball):
    pool = []

    for b in baseball:
        num = str(b[0])
        strike = b[1]
        ball = b[2]

        tempSet = set()

        for i in range(123, 987 + 1):
            sI = str(i)

            cntS = 0
            cntB = 0

            if sI[0] != '0' and sI[1] != '0' and sI[2] != '0' and sI[0] != sI[1] and sI[1] != sI[2] and sI[0] != [2]:
                for i in range(3):
                    for j in range(3):
                        if sI[i] == num[j] and i == j: cntS += 1
                        elif sI[i] == num[j] and i != j: cntB += 1

                if strike == cntS and ball == cntB:
                    tempSet.add(int(sI))

        pool.append(set(tempSet))

    res = pool.pop()
    for p in pool:
        res = res.intersection(p)

    return len(res)




if __name__ == '__main__':
    print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
