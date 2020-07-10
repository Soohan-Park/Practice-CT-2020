def solution(stock, dates, supplies, k):
    answer = 0

    today = 0
    for i in range(len(dates)):
        if today + stock >= k - 1: return answer

        restDayUntilSupp = (dates[i] - today) # 오늘을 포함해서
        restStock = stock - restDayUntilSupp

        if restStock == 0:
            today = dates[i]
            stock = supplies[i]
            answer += 1
        else:
            today = dates[i]
            if today + restStock >= k - 1: return answer
            elif today + restStock + supplies[i] >= k - 1: return answer + 1
            else:
                stock = restStock



    return answer


if __name__ == '__main__':
    print(solution(4, [4, 10, 15], [20, 5, 10], 30))