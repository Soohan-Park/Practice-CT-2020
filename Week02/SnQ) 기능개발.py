# Solved.

isEmpty = lambda x : True if len(x) == 0 else False


def solution(progresses, speeds):
    answer = []

    while not isEmpty(progresses):
        length = len(progresses)  # 남은 작업의 수
        progresses = [ progresses[i] + speeds[i] for i in range(length) ]  # 각 progress 에 speed 만큼 더하기
        
        if progresses[0] >= 100:  # 작업 순서 중 맨 첫번째 작업 수행도가 100 이상인 경우
            flag = True

            for i in range(length):
                if progresses[i] < 100:
                    answer.append(i)  # i == 수행도 100이 안되는 작업의 인덱스 == 수행도가 100 이상되는 작업의 갯수
                    progresses = progresses[i:]  # i번째 작업은 아직 수행도 100을 넘지 못한 상태
                    speeds = speeds[i:]
                    flag = False
                    break

            if flag:  # 남은 모든 작업의 수행도가 100 이상인 경우
                answer.append(length)
                progresses = []
        
    return answer


if __name__ == '__main__':
    print(solution([93,30,55], [1,30,5]))
