# BFS, DFS 어떻게 써야할지...


def solution(n, computers):
    #answer = 1

    book = dict().fromkeys(range(n), None)
    samePool = 0

    K = 0
    for com in computers:
        if 0 not in com: return 1

        if com.count(1) == 1:
            K += 1
        else:
            flag = True
            temp = None
            for i in range(len(com)):
                if com[i] == 1:
                    if book[i] is None:
                        if flag:
                            book[i] = K
                        else:
                            book[i] = temp
                    else:
                        flag = False
                        temp = book[i]

            if flag:
                K += 1


    return K


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))