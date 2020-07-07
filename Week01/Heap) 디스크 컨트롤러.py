def solution(jobs):
    import heapq as h

    jobs = sorted(jobs, key=lambda x: x[0])  # requestTime 기준으로 정렬.
    length = len(jobs)

    answer = 0
    endTime = 0
    pool = []

    isEmpty = lambda x : True if len(x) == 0 else False

    while True:
        if isEmpty(jobs):
            target = h.heappop(pool)

            answer += endTime - target[1]  # 대기시간
            answer += target[0]  # 수행시간
            endTime += target[0]

        else:
            job = jobs.pop(0)
            requestTime = job[0]
            spendingTime = job[1]

            if requestTime < endTime:
                h.heappush(pool, [spendingTime, requestTime]) # 풀에선 반대가 되어야함!

            else:
                if isEmpty(pool):
                    answer += spendingTime
                    endTime = (requestTime + spendingTime)

                else:
                    target = h.heappop(pool)

                    answer += endTime - target[1] # 대기시간
                    answer += target[0] # 수행시간
                    endTime += target[0]

                    h.heappush(pool, [spendingTime, requestTime])

        if isEmpty(pool) and isEmpty(jobs) : break

    answer = int(answer / length)

    return answer


if __name__ == '__main__':
    print(solution([[1, 9], [0, 3], [2, 6]]))