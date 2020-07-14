# Solved.

def solution(answers):
    # 수포자별 찍는 방법
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    spam = [0, 0, 0]  # 수포자별 맞은 갯수

    for i in range(len(answers)):
        target = answers[i]
        
        # 수포자별 문제를 맞았는지 판단 | 인덱스를 나눠줌으로 계속 반복해서 돌도록 구현
        if target == supo1[i % len(supo1)]: spam[0] += 1
        if target == supo2[i % len(supo2)]: spam[1] += 1
        if target == supo3[i % len(supo3)]: spam[2] += 1

    # 가장 많이 맞춘 사람 찾아서 answer에 append
    for i in range(len(spam)):
        if max(spam) == spam[i]: answer.append(i+1)

    return answer


if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
    print(solution([1,3,2,4,2]))