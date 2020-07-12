# Solved.

def solution(priorities, location):
    prioritiesIdx = list(range(len(priorities)))
    printedList = []

    while True:
        if len(priorities) > 1: # priorities에 1개 초과로 남아있는 경우
            target = priorities.pop(0)
            targetIdx = prioritiesIdx.pop(0)
            
            if target >= max(priorities):
                printedList.append(targetIdx)
            else:
                priorities.append(target)
                prioritiesIdx.append(targetIdx)
        else: # priorities에 원소가 1개 이하로 남아있는 경우
            printedList.append(prioritiesIdx[0]) # 마지막 남아있는 인덱스
            break

    return printedList.index(location) + 1


if __name__ == '__main__':
    print(solution([2,1,3,2], 2))
    print(solution([1,1,9,1,1,1], 0))