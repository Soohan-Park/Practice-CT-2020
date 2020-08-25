# The code has occurred RUNTIME ERROR.


def f(_people, _limit, _weight, _prevcount):
    if len(_people) < 1:
        return _prevcount

    _weight += _people.pop()

    for i in range(len(_people)-1, -1, -1):
        if _weight + _people[i] > _limit:
            pass
        else:
            _weight += _people.pop(i)

    _prevcount += 1
    return f(_people, _limit, 0, _prevcount)


def solution(people, limit):
    people.sort()

    answer = f(people, limit, 0, 0)

    return answer


if __name__ == '__main__':
    print(solution([10, 20, 50], 100))
