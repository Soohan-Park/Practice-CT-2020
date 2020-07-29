# 짝수/홀수로 나누어 다시 한 번 생각해보기


def solution(money:list):
    answer = 0

    length = len(money)
    for i in range(len(money)):
        house = money.copy()
        stolen = house[i]

        house[i] = -1
        house[(i-1) % length] = -1
        house[(i+1) % length] = -1

        target = max(house)
        while target >= 0:
            stolen += target

            idx = house.index(target)
            house[idx] = -1
            house[(idx-1) % length] = -1
            house[(idx+1) % length] = -1

            target = max(house)

        if stolen > answer:
            answer = stolen

    return answer


if __name__ == '__main__':
    print(solution([1, 2, 3, 1]))
