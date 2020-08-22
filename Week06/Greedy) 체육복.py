# Solved.


def solution(n, lost, reserve):
    answer = n

    newLost = []

    for l in lost:
        if l in reserve:
            reserve.pop(reserve.index(l))
        else:
            newLost.append(l)

    for l in newLost:
        if l - 1 in reserve:
            reserve.pop(reserve.index(l - 1))
        elif l + 1 in reserve:
            reserve.pop(reserve.index(l + 1))
        else:
            answer -= 1

    return answer
