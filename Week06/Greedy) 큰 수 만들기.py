# Need to more efficiently.


def solution(number, k):
    import itertools as i

    combi = i.combinations(number, len(number) - k)
    answer = "0"

    for C in combi:
        temp = ""
        for c in C:
            temp += c

        if int(answer) < int(temp):
            answer = temp

    return answer