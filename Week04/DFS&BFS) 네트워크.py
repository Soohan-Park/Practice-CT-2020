# Sovled with Solution.
# https://www.pymoon.com/entry/Programmers-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-DFS-%ED%92%80%EC%9D%B4-Java
# Comment. DFS를 사용해서 모든 노드들을 탐색한다.
#          동시에 DFS를 재귀로 함으로써, 방문 노드들은 0을 리턴하는 방식으로
#          시작 노드 - 하위 노드 - 하위 하위 노드 ... 순으로 탐색해 나간다.
#          그러다 최종적으로 시작노드들에 대한 모든 하위 노드들을 탐색한 후에는 1을 리턴함으로써
#          하나의 네트워크가 완성되었다는 것을 표현해준다. 이렇게 모든 노드들에 대해 방문 여부를 탐색하면서 반복한다.


def dfs(i, computers, visited):
    if visited[i] is True:
        return 0

    visited[i] = True

    for j in range(len(computers[i])):
        if computers[i][j] == 1:
            dfs(j, computers, visited)

    return 1


def solution(n, computers):
    answer = 0
    visited = [ False for x in range(n) ]

    for i in range(n):
        if visited[i] is not True:
            answer += dfs(i, computers, visited)

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
