# Solved.


def solution(arrangement):
    answer = 0
    stack = 0
    laserFlag = False # taret이 Laser 인지 판별하기 위한 Bool.

    for target in arrangement:
        if target == "(":
            laserFlag = True
            stack += 1
        else: # ")"
            if laserFlag:
                stack -= 1 # 레이저를 뜻하는 (를 제거
                answer += stack
            else:
                stack -= 1 # 자르고 남은 막대 끝부분을 제거
                answer += 1

            laserFlag = False

    return answer


if __name__ == '__main__':
    print(solution("()(((()())(())()))(())"))
    print(solution("((()))"))