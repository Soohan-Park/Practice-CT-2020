# Solved.


def f(_alphabet:str, _name, _currState, _pos:int, _preCount): # return Count
    # 현재 설정하고자 하는 알파벳
    if _name[_pos] != 'A':
        _preCount += min(len(_alphabet) - _alphabet.index(_name[_pos]), _alphabet.index(_name[_pos]))
        cur = _pos % len(_name)
        _name = _name[:cur] + "A" + _name[cur+1:]

    # 원하는 이름으로 되었는지 확인
    if _name == _currState:
        return _preCount

    # 양 옆으로 어디로 갈지 판단
    pos_count = 0
    right_pos = _pos + 1
    left_pos = _pos - 1

    while True:
        pos_count += 1

        if _name[right_pos % len(_name)] == 'A':
            right_pos = right_pos + 1
        else:
            _preCount += pos_count
            # 재귀
            return f(_alphabet, _name, _currState, right_pos, _preCount)


        if _name[left_pos % len(_name)] == 'A':
            left_pos = left_pos - 1
        else:
            _preCount += pos_count
            # 재귀
            return f(_alphabet, _name, _currState, left_pos, _preCount)


def solution(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    currState = "A" * len(name)

    answer = f(alphabet, name, currState, 0, 0)

    return answer
