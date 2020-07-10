# https://programmers.co.kr/learn/courses/30/lessons/42578
# Solved (Almost. - 테스트케이스 한개만 틀렸음.. // 질문 답글 보고 해결)


def solution(clothes):
    answer = 1

    sortedClothes = dict()
    keySet = sortedClothes.keys()

    for cloth in clothes:
        kinds = cloth[1]
        if kinds not in keySet: sortedClothes[kinds] = 0
        sortedClothes[kinds] += 1

    # 옷을 안 입는 것을 하나의 경우의 수로 두고, 이를 카운트!
    for key in keySet:
        answer *= sortedClothes[key] + 1

    # 경우의 수를 고려해서 카운트
    from itertools import combinations
    for r in range(1, len(keySet) + 1):
        for comb in combinati   ons(keySet, r):
            cnt = 1
            for c in comb:
                cnt *= sortedClothes[c]
            answer += cnt

    # 모두 안입는 경우 없으므로, 한가지 케이스 빼줌.
    return answer - 1


if __name__ == '__main__':
    target = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    print(solution(target))