# Solved.

def solution(triangle):
    pool = dict().fromkeys(range(len(triangle)), 0)
    pool[0] += triangle[0][0]

    for t in range(len(triangle) - 1):  # 마지막은 탐색 X
        tempPool = dict().fromkeys(range(len(triangle[t+1])), 0)
        for i in range(len(triangle[t])):
            value = pool[i]
            sameIdx = value + triangle[t+1][i]  # 같은 인덱스
            plusOneIdx = value + triangle[t+1][i+1]  # +1 인덱스

            tempPool[i] = max(tempPool[i], sameIdx)
            tempPool[i+1] = max(tempPool[i+1], plusOneIdx)

        for j in tempPool.keys():
            pool[j] = tempPool[j]

    return max(pool.values())


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))


"""
만약 층별로 갯수가 하나씩 증가한다고 가정한다면, (삼각형을 띄고 있다고 하니)

각 숫자들은 아래층에서 자기 인덱스, 자기 인덱스 + 1 의 두 숫자에만 접근 가능
항상 idx, idx+1이 존재!


pool = {
	lastIndex(key) : sumValues(value)
	...
          }

for t in range(len(triangle) - 1): # 가장 마지막은 굳이 순회를 안해도 됨
	for i in range(len(triangle[t])):
		value = pool[i]
		pool[i] = value + triangle[t+1][i]  # 같은 인덱스
		pool[i+1] = value + triangle[t+1][i+1]  # 다음 인덱스


인덱스가 동일한 경우, 값을 비교해서 머지를 해줘야한다
비교되는 두 값 중 큰 값을 넣어줌.

"""