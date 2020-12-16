# https://www.acmicpc.net/problem/14501

def f(cur, visited, schedule, earn):
    if cur == len(schedule):
        return earn

    if not visited[cur]:
        earn += schedule[cur][1]

        for i in range(schedule[cur][0]):
            visited[cur+i] = True

    return f(cur+1, visited, schedule, earn)


def solution(N, schedule):
    visited = [ False for _ in range(len(schedule)) ]
    
    # 상담 불가 건수 제외
    for i in range(len(schedule)):
        if i+schedule[i][0] > N:
            visited[i] = True

    answer = []
    for i in range(len(schedule)):
        answer.append(f(i, visited.copy(), schedule, 0))

    return max(answer)


if __name__ == '__main__':
    print(solution(
        N=7,
        schedule=[
            [3, 10],
            [5, 20],
            [1, 10],
            [1, 20],
            [2, 15],
            [4, 40],
            [2, 200]
        ]
    ))