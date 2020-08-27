# Solved.


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


if __name__ == '__main__':
    print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
    print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))