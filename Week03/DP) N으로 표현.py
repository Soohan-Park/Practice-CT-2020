# Test Case 2, 3, 5번이 틀림.
# Solved with Solution.
# https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# Comment: 문제 접근 방법에 대해 감을 못 잡았던 것 같다.
#          참고한 솔루션에서 했던 접근 방법은,
#          1) 결과로 N 사용횟수를 return 해야하므로 N 사용 횟수에 따라 집합을 만들고 만들 수 있는 숫자들을 저장(총 8단계까지만 확인하면 되니)
#          2) 다음 단계(각 단계는 N의 사용 횟수)로 넘어가기 전, 집합 속 number가 있다면 해당 단계를 return.
#          3) N =3 일 때, N=1, 2와 N=2,1 은 중복이므로 가능 케이스의 절반까지만 확인하면 된다.

def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)

    return -1


"""
def solution(N, number):
    if N == number: return 1
    else:
        combNum = [ int(str(N) * x) for x in range(1, 8) ]
        pool = set()
        pool.add(N)

        for i in range(2, 8):
            tempPool = set()
            for target in pool:
                for j in range(0, i-1):
                    comb = combNum[j]

                    plus = target + comb
                    minus = target - comb
                    multi = target * comb
                    divid = target // comb  # 나머지 고려 X

                    if plus >= 0: tempPool.add(plus)
                    if minus >= 0: tempPool.add(minus)
                    if multi >= 0: tempPool.add(multi)
                    if divid >= 0: tempPool.add(divid)

                if number in tempPool: return i
                else: pool = tempPool

    return -1


if __name__ == '__main__':
    print(solution(5, 12))
    print(solution(2, 11))
    print(solution(5, 31168))
"""