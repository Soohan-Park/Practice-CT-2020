res = []


def dfsR(_numbers: list, _cur: int, _sign: bool, _value: int):
    if _cur == len(_numbers):
        res.append(_value)

    else:
        nowValue = _numbers[_cur]
        if not _sign:
            nowValue *= -1

        _value += nowValue  # 값 출력

        # 순차 호출
        dfsR(_numbers, _cur + 1, True, _value)  # +
        dfsR(_numbers, _cur + 1, False, _value)  # -


def solution(numbers: list, target: int):
    answer = 0

    dfsR(numbers, 0, True, 0)  # +로 시작
    dfsR(numbers, 0, False, 0)  # -로 시작

    for r in res:
        if r == target: answer += 1

    # 마지막 인덱스에서 두번 출력됨...ㅠ
    return answer // 2