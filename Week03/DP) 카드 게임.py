# 정확성 테스트 케이스 2, 10, 11 실패
# 효율성 테스트 케이스 2, 3 실패
# 동일한 숫자의 카드인 경우 고려해서 수정해보기!


def solution(left, right):
    answer = 0

    pl = 0
    pr = 0
    isEmpty = lambda p, deck : True if p > len(deck) - 1 else False

    while not isEmpty(pl, left) and not isEmpty(pr, right):
        if max(left) < right[pr]:
            pl += 1
            pr += 1
        else:
            if left[pl] > right[pr]:
                answer += right[pr]
                pr += 1
            else:
                # 아래의 조건문으로는 해결이 안 됨.
                if max(left[pl:]) == max(right[pr:]):  # 남은 카드들 중에서 동일한 거!!
                    pr += 1
                pl += 1

    return answer