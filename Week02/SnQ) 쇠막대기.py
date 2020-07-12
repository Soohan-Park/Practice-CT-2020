# Solved.

def solution(arrangement):
    answer = 0
    stack = 0
    lazerFlag = False # taret이 Lazer 인지 판별하기 위한 Bool.

    for target in arrangement:
        if target == "(":
            lazerFlag = True
            stack += 1
        else: # ")"
            if lazerFlag:
                stack -= 1 # 레이저를 뜻하는 (를 제거
                answer += stack
            else:
                stack -= 1 # 자르고 남은 막대 끝부분을 제거
                answer += 1

            lazerFlag = False

    return answer


if __name__ == '__main__':
    # print(solution("()(((()())(())()))(())"))
    print(solution("((()))"))