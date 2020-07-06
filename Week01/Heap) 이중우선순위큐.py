# Solved.

def solution(operations):
    queue = []

    for operation in operations:
        op, val = operation.split(" ")

        if op == "I": queue.append(int(val))
        elif op == "D" and len(queue) != 0:
            if int(val) > 0: queue.pop(queue.index(max(queue)))
            else: queue.pop(queue.index(min(queue)))

    if len(queue) == 0: return [0, 0]
    else: return [max(queue), min(queue)]


if __name__ == '__main__':
    print(solution(["I 16", "D 1"]))
    print(solution(["I 7", "I 5", "I -5" , "D -1"]))