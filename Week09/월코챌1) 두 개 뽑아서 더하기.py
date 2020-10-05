# Solved

def solution(numbers):
    from itertools import combinations
    answer = set()

    pool = combinations(numbers, 2)
    for p in pool:
        answer.add(p[0] + p[1])

    return sorted(list(answer))


if __name__ == '__main__':
    print(solution([2, 1, 3, 4, 1]))