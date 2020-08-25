def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for c in completion:
        for p in participant:
            if c == p:
                participant.remove(p)
                break
            else:
                pass
    answer = participant.pop()

    return answer