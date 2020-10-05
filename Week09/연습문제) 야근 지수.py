# Solved.
# log(n)으로 만드는 것이 중요!
# 코드가 짧다고 좋은 것이 아니다!
# 입력 하나당 한번의 연산을 하는 경우 O(n) -> 즉 1~n 까지 모두 검색하는 경우
# 조건에 따라, 입렵당 연산을 하는 횟수가 줄어드는 경우(물론 입력의 크기에 따라 처리 시간은 증가하나, 조건에 따라 그 증가폭이 1:1 보다 작은 경우) O(logn)

# Big-O : logn
def solution_logn(n, works):
    answer = 0
    idx = 0
    size = len(works)
    
    works.sort(reverse=True)  # 내림차순 정렬

    if sum(works) <= n:
        return 0

    while True:
        if idx == size - 1:  # 맨 마지막 원소일 경우
            for i in range(n):
                works[i % size] -= 1
            break
        else:
            if works[idx] == works[idx+1]:  # 두 원소가 같을 때
                if idx < n:
                    idx += 1
                else:
                    for i in range(n):
                        works[i] -= 1
                    break

            else:  # 두 원소가 다른 경우
                count = idx + 1
                if n - count > 0:
                    for i in range(count):
                        works[i] -= 1
                    n -= count
                    idx = 0
                else:
                    for i in range(n):
                        works[i] -= 1
                    break

    for w in works:
        answer += w ** 2

    return answer


# Big-O : n
def solution_n(n, works):
    answer = 0

    works.sort(reverse=True)

    if sum(works) <= n:
        return 0

    for i in range(n):
        idx = works.index(max(works))
        works[idx] -= 1

    for w in works:
        answer += w ** 2

    return answer


if __name__ == '__main__':
    print(solution_logn(4, [4, 3, 3]))
    print(solution_logn(1, [2, 1, 2]))
    print(solution_logn(3, [1, 1]))


"""
야근 지수 = 야근을 시작한 시점에서, 남은 일의 작업량 ** 2 하여 모두 더한 값


만약, works의 총 합이 n 보다 작거나 같으면 return 0

n번만큼 반복
    works 내 max값에 -1

return works에서 제곱한 값을 모두 누적    
"""
