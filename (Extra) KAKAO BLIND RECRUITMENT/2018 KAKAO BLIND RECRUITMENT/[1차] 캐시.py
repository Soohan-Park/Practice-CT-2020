# Solved.


def solution(cacheSize, cities):
    answer = 0

    if cacheSize == 0:
        return 5 * len(cities)

    cache = [ None ] * cacheSize
    LRUIndex = [ x for x in range(cacheSize - 1, -1, -1) ]

    for city in cities:
        city = city.lower()

        if city in cache:
            idx = cache.index(city)
            LRUIndex.insert(0, LRUIndex.pop(LRUIndex.index(idx)))
            answer += 1
        else:
            idx = LRUIndex.pop()
            cache[idx] = city
            LRUIndex.insert(0, idx)
            answer += 5

    return answer


if __name__ == '__main__':
    print(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']))
    print(solution(5, ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']))



"""
cacheSize 만큼 캐시를 만든다
각 캐시 자리에 따른 최근 사용을 기록할 리스트를 만든다
ex. cacheSize가 3이면, [2, 1, 0]
    역순으로 만들어서 제일 아래쪽(0)부터 캐시가 기록되도록 구성!
    해당 공간을 Read&Write하면 리스트 제일 앞으로!
    [2, 1, 0] -> [0, 2, 1]
    따라서, 제일 뒤에 있는 인덱스가 가장 오랫동안 사용이 안된 공간.

도시이름을 하나 가져와서 toLower 처리. (소문자로 처리하자)
캐시 안에 도시 이름이 있는지 비교
    있으면, 해당 캐시 최근 사용 리스트 앞으로 빼주고, answer += 1
    없으면, 캐시 공간이 있는지 확인
        있으나 없으나 동일하게, 최근 사용 리스트 가장 마지막 인덱스에 해당하는 공간에 저장 & answer += 5

한바퀴 돈 후 최종 RETURN answer
"""
