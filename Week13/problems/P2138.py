# BFS
# 불가능한 경우를 어떻게 판별?
def run():
    N = int(input())
    target = input()
    result = input()

    print(bfs(target, result, f(target), 1))


def bfs(target, result, queue, cnt):
    if result in queue:
        return cnt

    newQueue = set()
    for q in queue:
        newQueue.join(f(q))

    return bfs(target, result, newQueue, cnt + 1)


def f(target):
    res = set()
    for i in range(len(target)):
        temp = target

        if i == 0:
            temp = tog(temp[:2]) + temp[2:]
        elif i == len(target) - 1:
            temp = temp[:-2] + tog(temp[-2:])
        else:
            temp = temp[:i - 1] + tog(temp[i - 1:i + 2]) + temp[i + 2:]

        res.add(temp)

    return res


def tog(subTartget):
    res = ''
    for sub in subTartget:
        res += '1' if sub == '0' else '0'
    return res
