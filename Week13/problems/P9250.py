def solution(N, S, Q, words):
    for word in words:
        print(f(S, word))


def f(S, word):
    for s in S:
        if s in word: return 'YES'
    return 'NO'


def run():
    _N = int(input())
    _S = [input() for _ in range(_N)]
    _Q = int(input())
    _words = [input() for _ in range(_Q)]

    solution(
        N=_N,
        S=_S,
        Q=_Q,
        words=_words
    )