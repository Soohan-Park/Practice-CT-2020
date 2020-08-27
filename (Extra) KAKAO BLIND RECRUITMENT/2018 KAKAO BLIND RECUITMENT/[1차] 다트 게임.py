# Solved by myself.
# BUT THIS CODE MUST BE MORE EFFIECIENTLY.

# 스택을 사용해서 한번 바꿔보자!!!! (왜 스택을 생각하지 못했을까..ㅠ)


def solution(dartResult : str):
    size = len(dartResult)
    i = 0
    buff = None
    scoreIdx = 0
    scores = [0, 0, 0]
    flag = True  # 스타상|아차상 처리를 위한 Flag.

    while i < size - 1:  # 마지막 문자 체크 X
        target = dartResult[i]

        if flag:
            if target.isnumeric():
                if target == '1' and dartResult[i+1] == '0':
                    buff = 10
                    i += 1
                else:
                    buff = int(target)
            elif target in ['S', 'D', 'T']:
                # "SDT".index(target) + 1 같이 간소화 가능할 듯!
                if target == 'S': buff = buff ** 1
                elif target == 'D': buff = buff ** 2
                elif target == 'T': buff = buff ** 3

                if dartResult[i+1].isnumeric():
                    scores[scoreIdx] = buff
                    buff = None  # buff 초기화가 굳이 필요는 없을 수도 있다! (하지만 안정성 측면에서는 있는게 좋을지도)
                    scoreIdx += 1
                else:
                    flag = False # 다음 루프에서 스타상|아차상 처리
                    scores[scoreIdx] = buff
                    buff = None
        else:
            if target == '*':
                scores[scoreIdx] = scores[scoreIdx] * 2
                if scoreIdx != 0:
                    scores[scoreIdx - 1] = scores[scoreIdx - 1] * 2
            elif target == '#':
                scores[scoreIdx] = scores[scoreIdx] * -1

            flag = True
            scoreIdx += 1

        i += 1

    lastTarget = dartResult[-1]
    if lastTarget in ['S', 'D', 'T']:
        if lastTarget == 'S': scores[scoreIdx] = buff ** 1
        elif lastTarget == 'D': scores[scoreIdx] = buff ** 2
        elif lastTarget == 'T': scores[scoreIdx] = buff ** 3
    else:
        if lastTarget == '*':
            scores[scoreIdx] = scores[scoreIdx] * 2
            if scoreIdx != 0:
                scores[scoreIdx - 1] = scores[scoreIdx - 1] * 2
        elif lastTarget == '#':
            scores[scoreIdx] = scores[scoreIdx] * -1

    return sum(scores)


if __name__ == '__main__':
    print(solution("1S2D*3T"))
    print(solution("1T2D3D#"))



"""
각 기회마다 얻을 수 있는 점수의 범위 -> 0~10

S: score^1
D: score^2
T: score^3

*: 스타상 | 해당 기회의 점수 & 그 전 점수 2배로!스
    스타상이 첫번째 기회에 나오면 첫번째만 두배
    스타상 효과는 중첩 가능 (4배 || 최대 4배까지만 가능함) 
#: 아차상 |  해당 점수는 마이너

스타상과 아차상 효과는 중첩 가능! (이럴경우 -2배가 됨!)


문자열 하나씩 쪼개서 가져옴
size - 1 만큼 반복을 함! (마지막꺼는 마지막에 따로 처리)
하나 가져오고 그 다음 글지가 숫자인지 판단 (10 때문에)
"""
