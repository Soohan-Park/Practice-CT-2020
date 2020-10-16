# Bottom-up 피보나치

def f(N):

    if N in (1, 2):
        return 1

    first = 1
    second = 1

    for i in range(N-2):
        temp = first + second
        first = second
        second = temp

    return second


ans = f(int(input()))
print(ans)

"""
N = 3 이라면, 10진수로 4~7에 해당 (2^(N-1) ~ 2^N - 1)
"""
10000

10001

10010
10011
10100

10101
10110
10111



1000

1001
1010
1011

1100
1101
1110

1111

1, 2, 3, 4, 5, 6,
0, 1, 2, 3, 5, 8

10
11