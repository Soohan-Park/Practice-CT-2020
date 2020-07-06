def solution(genres, plays):
    answer = []

    length = len(plays) # genres.__len__ == plays.__len__
    setGenres = set(genres)
    #dictionary = dict().fromkeys(genres, [0 for x in range(length + 1)]) => ERR! value 값의 리스트가 동일한 아이디를 가짐
    dictionary = dict()
    for genre in setGenres:
        dictionary[genre] = [ 0 for x in range(length + 1)] # 리스트 마지막이 장르별 총 재생횟수

    # 데이터 정제
    for i in range(length):
        dictionary[genres[i]][i] = plays[i]
        dictionary[genres[i]][length] += plays[i] # 장르별 총 재생 횟수

    # 장르별 총 재생 횟수 순으로 정렬
    dictValues = sorted(dictionary.values(), key=lambda x : x[length], reverse=True)

    for value in dictValues:
        # 총 재생 횟수 제거
        value[length] = 0

        # 장르 내 첫번째 대상
        idx = value.index(max(value))
        answer.append(idx)
        value[idx] = 0

        # 장르 내 두번째 대상
        if max(value) != 0 :
            idx = value.index(max(value))
            answer.append(idx)

    return answer


if __name__ == '__main__':
    print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))