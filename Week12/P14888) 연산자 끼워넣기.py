from itertools import permutations

def solution(N, nums, opers):
    answer = []
    operPool = []

    for i in range(4):
        operPool.extend( ['+-*/'[i] for _ in range(opers[i])] )

    operList = permutations(operPool, N-1)

    for oper in operList:
        spam = nums.copy()
        oper = list(oper)

        n1 = spam.pop(0)
        for _ in range(len(oper)):
            n2 = spam.pop(0)
            op = oper.pop(0)
            n1 = calc(n1, op, n2)

        answer.append(n1)

    answer.sort()

    return [answer[-1], answer[0]]


def calc(n1, op, n2):
    if op == '+':
        return n1+n2
    elif op == '-':
        return n1-n2
    elif op == '*':
        return  n1*n2
    else:
        return (n1 // n2) if n1 >= 0 else (-1 * abs(n1 // n2))


if __name__ == '__main__':
    print(solution())