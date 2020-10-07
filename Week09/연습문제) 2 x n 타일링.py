# 아래 링크의 방식에 의하면 결국엔 피보나치 수열이라고 함..
# https://deveric.tistory.com/61
# 그림을 n-4까지 그려보면 알게 됨! (이전 두 개의 스텝의 것들이 전부 포함되어 있음)
# 점화식에서 F(1)은 맨 처음 케이스의 경우의 수가 몇개인지!
#
# DP 문제는 케이스를 나누는 것이 중요!!
# 케이스를 나눌 때 해결하기 직전부터 거꾸로 생각해보며 접근!
# DP 문제를 더 풀어봐야겠다.

def solution(n):
    a, b = 1, 1
    for _ in range(n-1):
        c = (a + b) % 1000000007
        a = b
        b = c
    return b


# def solution(n):
#     answer = 0
#
#     fact = lambda _x: 1 if _x <= 1 else _x * fact(_x - 1)
#     nPr = lambda _n, _r: fact(_n) / fact(_n - _r)
#     nCr = lambda _n, _r: nPr(_n, _r) / fact(_r)
#
#     isEven = lambda _n: _n % 2 == 0
#
#     r = 0
#
#     if isEven(n):
#         times = n // 2
#     else:
#         times = n // 2 + 1
#
#     for _ in range(n, times-1, -1):
#         answer += int(nCr(n, r))
#         n -= 1
#         r += 1
#         # answer = answer % 1000000007
#
#     return answer % 1000000007


if __name__ == '__main__':
    print(solution(52))


"""
1 & 2 로 n 을 만드는 경우의 수

1 : 1
2 : 2
3 : 3
4 : 1 1 1 1
    1 1 2 * 3
    2 2
5 : 1 1 1 1 1
    1 1 1 2 * 4
    1 2 2 * 3

6 : 1 1 1 1 1 1
    1 1 1 1 2
    1 1 2 2
    2 2 2

    1 1 1 1 2 2
nCr
n : 전체 자리 수
r : 2의 수

n! / n-r!

3 2 1
2 1
"""