# Solved.


def solution(heights):
    answer = []

    # 리스트의 역순으로 탐색
    for i in range(len(heights) - 1, 0, -1):
        flag = True  # 자신보다 왼쪽에 있는 타워들 중 자신보다 큰 게 없는 경우를 위한 플래그
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer.insert(0, j+1)
                flag = False
                break

        # 자신보다 왼쪽에 있는 타워들 중 자신보다 큰 게 없는 경우 0 삽입
        if flag: answer.insert(0, 0)

    # 맨 왼쪽에 있는 타워를 위해 0 삽입
    answer.insert(0, 0)

    return answer


if __name__ == '__main__':
    print(solution([3, 9, 9, 3, 5, 7, 2]))
