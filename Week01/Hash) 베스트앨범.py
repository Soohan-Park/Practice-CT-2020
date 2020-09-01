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



"""
- 각 장르별 재생수가 가장 많은 2곡씩 선택 (1곡만 있으면 1곡만)
- 선택 기준
	1. 장르별 재생 수 높을수록 먼저 수록
	2. 장르 내에서 많이 재생된 노래 먼저 수록
	3. 장르 내 재생 횟수가 같다면, 고유 번호가 낮은거 먼저!
	   (인덱스가 낮은걸 먼저)

- 유의 사항
	1. 모든 장르는 재생된 회수가 다름
	2. 만약 두번째 곡이 재생횟수가 동일한 곡이 2곡 이상이라면?
		=> 인덱스 가장 낮은거만 수록
- 접근 방법
	* 데이터 정리가 중요할 듯
	1. 딕셔너리
		{ 장르 : [ 인덱스 순으로 재생횟수 (해당 안되는 것은 0) , 장르별 총 횟수]}
	
	2. 장르별 총 재생 횟수 먼저 떼내서 비교 후 장르 별 순서 정함
		=> 여기서부턴 장르가 무엇인지 안중요함!
		=> 딕셔너리에서 밸류값만 따로 떼어내서 정리	
	3. 각 장르 내에서 순서 정하기
	4. max 로 가장 높은 값 인덱스 리턴 후, 해당 값 -1
	5. 다음으로 max 로 가장 높은 값 인덱스 리턴 (어차피 인덱스 가장 낮은거 리턴)
		=> (선택 기준 3번 해결)
"""