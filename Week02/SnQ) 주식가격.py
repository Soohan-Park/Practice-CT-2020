# Solved.


def solution(prices):
    answer = []
    length = len(prices)
    minPrice = min(prices)  # 약간의 수행시간을 더 줄여줌. ex) 128ms -> 106ms

    for i in range(0, length - 1):  # 맨 마지막은 비교 대상이 없어, 무조건 0
        if prices[i] == minPrice: answer.append(length - i - 1)
        else:
            flag = True
            for j in range(i+1, length):
                if prices[j] < prices[i]:
                    flag = False
                    answer.append(j - i)
                    break

            if flag: answer.append(length - i - 1)

    answer.append(0)

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 2, 3]))
    print(solution([1, 1, 1, 1, 1, 1]))
    print(solution([5, 4, 3, 2, 1]))
