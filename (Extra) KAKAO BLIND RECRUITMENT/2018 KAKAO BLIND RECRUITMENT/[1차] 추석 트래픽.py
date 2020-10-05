def solution(lines):
    answer = 0
    return answer


"""
Queue을 사용해야할 듯 하다.

모든 로그 끝나는 시간에 +1초 한다. (초당 최대 처리량 = 임의의 시점에서 1초동안 처리되는 갯수)
Queue을 이용해서 Stack에 들어가있는 최대 값이 정답이 된다.
Queue에 값을 넣을 때, 넣고 len(STACK)과 answer 비교 후 더 크면 answer 대체.
Queue에 값을 뺄 때는 별도 처리 없이 그냥 빼면 된다.

시작시간 = 처리시간 - 소요시간 + 0.001




lines 반복
    
"""