# Solved. (Using BFS)
# 문제에서 target이 words 안에는 존재하지만, 변환할 수 없는 경우에 대한 케이스가 추가적으로 필요할 것 같다.


def solution(begin, target, words):
    if target not in words:  # 변환할 수 없는 경우 (target이 words에 없으면 변환할 수 없다)
        return 0
    else:
        stackA = [ begin ]
        stackB = []

        count = 0
        while True:
            count += 1
            for a in stackA:
                for w in words:
                    if a != w:
                        cntDiff = 0
                        for i in range(len(a)):  # len(a) == len(w)
                            if a[i] != w[i]:
                                cntDiff += 1

                                if cntDiff >= 2:
                                    break

                        if cntDiff == 1:
                            stackB.append(w)

            if target in stackB:
                return count

            stackA = stackB
            stackB = []
