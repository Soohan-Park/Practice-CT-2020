# Solved.


def solution(numbers):
    from itertools import permutations

    pool = list()  # numbers로 가능한 수 조합 생성
    for i in range(len(numbers)):
        pool.append(permutations(numbers, i+1))

    pool2 = set()  # 생성된 조합들을 숫자로 변환
    for p in pool:
        for target in p:  # target == ('0', '1',)
            temp = ""
            for t in target:
                temp += t
            pool2.add(int(temp))

    answer = 0
    pool2.discard(0) # 0, 1 제거 | discard() 써야 poo2 에 0, 1이 없어도 예외가 발생하지 않음
    pool2.discard(1)
    for p in pool2:  # 소수 판별
        flag = True
        for i in range(2, p):
            if p % i == 0:
                flag = False
                break
        if flag: answer += 1

    return answer


if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))
