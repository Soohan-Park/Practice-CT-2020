# Solved.


def solution(str1, str2):
    strSet1 = []
    strSet2 = []

    for i in range(len(str1) - 1):
        if not str1[i].isalpha(): continue
        if not str1[i+1].isalpha(): continue
        strSet1.append( (str1[i] + str1[i+1]).lower() )

    for i in range(len(str2) - 1):
        if not str2[i].isalpha(): continue
        if not str2[i+1].isalpha(): continue
        strSet2.append( (str2[i] + str2[i+1]).lower() )

    cntGyo = 0
    cntHap = 0
    gyo = set(strSet1) & set(strSet2)
    hap = set(strSet1) | set(strSet2)

    for g in gyo:
        cnt1 = strSet1.count(g)
        cnt2 = strSet2.count(g)

        if cnt1 == cnt2:
            cntGyo += cnt1  # cnt1 == cnt2
        else:
            cntGyo += min(cnt1, cnt2)

    for h in hap:
        cnt1 = strSet1.count(h)
        cnt2 = strSet2.count(h)

        if cnt1 == cnt2:
            cntHap += cnt1  # cnt1 == cnt2
        else:
            cntHap += max(cnt1, cnt2)

    answer = 65536 if cntHap == 0 else int((cntGyo / cntHap) * 65536)

    return answer


if __name__ == '__main__':
    print(solution("FRANCE", "french"))
    print(solution("handshake", "shake hands"))
    print(solution("aa1+aa2", "AAAA12"))



"""
자카드 유사도 -> 교집합 / 합집합

입력으로 들어온 두 문자열을 두 글자씩 끊어서, 다중집합의 원소로 만듬
영문자만 유효! (이외 문자가 있는경우 버림)
문자열의 대소문자 구분 X -> lower 처리

두 문자에 대한 유사도 구한 후, 65536 곱하고 소수점 아래 버림.

1. 입력으로 들어온 문자열 두 글자씩 처리
   동시에, 영문자가 아닌 경우는 날리기

2. set으로 해서 두 다중집합에서 교집합 뽑아냄
   교집합 원소들을 하나씩 반복하면서, 각 원소마다 두 집합에 몇 개씩 있는지 확인
   두 집합에서 해당 원소의 갯수가 같다면, 해당 숫자만큼 카운트!
   두 집합에서 해당 원소의 갯수가 다르다면, 두 수 중 작은 숫자만큼 카운트!
   교집합 원소들로 카운트 후 누적 값 사용

3. set으로 해서 두 다중집합에서 합집합 뽑아냄
   합집합 원소들을 하나씩 반복하면서, 각 원소마다 두 집합에 몇 개씩 있는지 확인
   두 집합에서 해당 원소의 갯수가 같다면, 해당 숫자만큼 카운트!
   두 집합에서 해당 원소의 갯수가 다르다면, 두 수 중 큰 숫자만큼 카운트!
   합집합 원소들로 카운트 후 누적값 사용

4. 2번 / 3번 값에 65536 곱하고 int()
"""
