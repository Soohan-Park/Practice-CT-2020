# Solved.

def solution(N):
    if N == 1: return 4
    if N == 2: return (1 + 2) * 2
    else:  # N은 3 이상
        n2 = 1  # n-2
        n1 = 1  # n-1

        N = N - 2
        for i in range(N):
            # n = (n-1) + (n-2) || 피보나치 수열
            n = n1 + n2
            n2 = n1
            n1 = n

        return (n1 + (n1 + n2)) * 2


if __name__ == '__main__':
    print(solution(6))