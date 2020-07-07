def solution(scoville, K):
    import heapq

    heapq.heapify(scoville)
    L = len(scoville)

    f = heapq.heappop(scoville)
    for i in range(1, L):
        s = heapq.heappop(scoville)
        f = heapq.heappushpop(scoville, f + s * 2)
        if f >= K: return i

    return -1


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 5, 4, 10, 12], 7))