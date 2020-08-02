# Solved! But.. Efficiency is worst.

def solution(citations):
    citations.sort(reverse=True)

    # H는 배열안의 수가 아닐 수도 있다!!
    # 탐색 범위 => 최대: H번 이상 인용되어야 하므로, 최대 인용된 횟수
    #              최소: H 번 이상, H 번 이하 인용되어야 하므로, 최소 인용 횟수
    for i in range(len(citations)):
        for H in range(citations[i], -1, -1):
            moreThanH = citations[:i + 1]  # H편 이상 인용!
            lessThanH = citations[i + 1:]  # 나머지! 논문들

            if len(moreThanH) >= H and len(lessThanH) <= H:
                minMoreThanH = moreThanH[-1]  # moreThanH의 마지막이 최솟값.
                if len(lessThanH) == 0:
                    maxLessThanH = 0
                else:
                    maxLessThanH = lessThanH[0]  # lessThanH의 첫번째가 최댓값.


                if minMoreThanH >= H and maxLessThanH <= H:
                    return H
        
    return 0



if __name__ == '__main__':
    print(solution([1, 0]))
    print(solution([3, 0, 6, 1, 5]))
    print(solution([6, 5, 3, 3, 2, 1, 0]))
    print(solution([5, 5, 5, 5]))