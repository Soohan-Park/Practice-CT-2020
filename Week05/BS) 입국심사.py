# Solved with Solution.
# https://woongsin94.tistory.com/185
# Comment: "추정 시간값 / 각 심사관별 심사시간 = 심사관당 맡을 수 있는 입국자 수"
#          시간을 기준으로 특정 시간을 주고, 그 시간에 해결가능한지 판단!
#          안된다면 이분탐색으로 다음 가능한 시간 찾기!
#          즉, 예상되는 총 심사 시간을 최대 예상 시간과 최소 예상 시간의 중간값부터 시작해서 찾아 나선다
#          각 예상 시간안에 심사관들이 모든 입국자를 심사 할 수 있는지 판단!
#
#          => 명확히 주어진 대상만이 탐색대상이 아니다!! 명확하게 보이지 않을 때는 다른 대상으로 탐색을 시도해보자!


def solution(n, times):
    size = len(times)
    minimum = 1
    maximum = times[-1] * n
    answer = maximum  # 예상되는 시간들 중 가장 큰 시간

    # 이진 탐색
    while minimum <= maximum:
        middle = (minimum + maximum) // 2  # middle == 예상되는 총 심사 시간!!
        summ = 0  # 예상되는 심사 가능한 입국자 수
        for i in range(size):
            summ += middle // times[i]  # 한 심사관당 담당 입국자 수

        if n > summ:
            minimum = middle + 1
        else:
            if middle <= answer:
                answer = middle
            maximum = middle - 1

    return answer


if __name__ == '__main__':
    print(solution(6, [7, 10]))
