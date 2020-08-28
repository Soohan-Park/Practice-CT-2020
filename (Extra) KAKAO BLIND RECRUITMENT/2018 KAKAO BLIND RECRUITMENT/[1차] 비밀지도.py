# Solved.


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # arr1
        n1 = bin(arr1[i])[2:]
        n1 = '0' * (n - len(n1)) + n1  # 이진수의 자릿수 맞추기 위해

        # arr2
        n2 = bin(arr2[i])[2:]
        n2 = '0' * (n - len(n2)) + n2

        spam = ""
        for j in range(n):
            spam += '#' if int(n1[j]) | int(n2[j]) else ' '  # OR 연산

        answer.append(spam)

    return answer


if __name__ == '__main__':
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))


"""
지도는 NxN의 정사각 배열.
각 지도에서 하나라도 벽이면 벽.
모두 공백이라면 전체에서도 공백.
    -> OR 연산 필요. (1이 벽, 0이 공백)

입력은 십진수로 들어옴
들어온 십진수를 이진수로 변환 (한변의 길이 n만큼 앞에 0을 덧붙이는 작업이 필요할 듯함)

두 배열에 대해 이진수로 변환한 뒤 OR 연산.
합쳐진 그림에 대해, 0이면 ' ' & 1이면 '#' 처리해서 각 줄당 문자열로 만들어 배열에 넣어서 Return.

NEED TO DEVELOP.
   1) 십진수 -> 이진수
   2) OR 연산
   3) 출력
"""
