# Solved.

def solution(brown, yellow):
    from math import sqrt

    factorizationYellow = []  # 소인수분해
    for i in range(1, int(sqrt(yellow)) + 1):
        if yellow % i == 0:
            factorizationYellow.append( [yellow // i, i] )

    # 소인수분해한 조합에서, 가로&세로에 +2 해주고
    # (갈색타일이 노란타일을 감싸고 있는 형태이기 때문에, 위&아래로 2줄이 각각 늘어남)
    # 가로 세로를 곱한 것이 결국 전체 타일, 즉 갈색 + 노란색이 된다.
    for f in factorizationYellow:
        target = [ x+2 for x in f ]
        if target[0] * target[1] == brown + yellow: return target

    # 문제에서 답이 없는 경우는 주어지지 않으므로, 위와 같이 조건문 안에서 반드시 리턴이 나옴.


if __name__ == '__main__':
    print(solution(24, 24))