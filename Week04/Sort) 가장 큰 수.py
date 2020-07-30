# 10 으로 나눈 나머지가 큰 순서대로 정렬
# 순서대로 문자열로 만들어서 붙임 -> 리턴

# 뭐가 문제인지...
# 세자리, 두자리, 한자리 이렇게 있는 경우에 대해 "맨뒷자리 정렬" 고민이 필요할 것으로 보인다.


def solution(numbers):
    answer = ''

    numbers = sorted(numbers, key=f, reverse=True)  # 맨 앞자리 기준으로 정렬

    pool = []
    target = numbers.pop(0)
    while len(numbers) != 0:

        if f(target) == f(numbers[0]):
            pool.append(target)
        else:
            if len(pool) != 0:
                pool = sorted(pool, key=lambda x : x % 10, reverse=True)  # 맨 뒷자리 기준으로 정렬
                for p in pool:
                    answer += str(p)
                pool = []
            else:
                answer += str(target)

        target = numbers.pop(0)

    if len(pool) != 0:
        pool.append(target)
        pool = sorted(pool, key=lambda x: x % 10, reverse=True)
        for p in pool:
            answer += str(p)
    else:
        answer += str(target)

    return str(int(answer))  # 0000 방지


def f(x:int):
    return int(str(x)[0]) if len(str(x)) > 1 else x



if __name__ == '__main__':
    print(solution([3, 30, 34, 5, 9]))
    print(solution([6, 19, 2]))
    print(solution([0,0,0,0]))