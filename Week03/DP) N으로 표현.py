# Test Case 1, 5, 6, 7 이 틀림.


def solution(N, number):
    if N == number: return 1
    else:
        combNum = [ int(str(N) * x) for x in range(1, 8) ]
        pool = set()
        pool.add(N)

        for i in range(2, 8):
            tempPool = set()
            for target in pool:
                for j in range(i - 1):
                    comb = combNum[j]

                    plus = target + comb
                    minus = target - comb
                    multi = target * comb
                    divid = target // comb  # 나머지 고려 X

                    if plus >= 0: tempPool.add(plus)
                    if minus >= 0: tempPool.add(minus)
                    if multi >= 0: tempPool.add(multi)
                    if divid >= 0: tempPool.add(divid)

            if number in tempPool: return i - 1
            else:
                pool = tempPool

    return -1


if __name__ == '__main__':
    print(solution(5, 12))
    print(solution(2, 11))
    print(solution(5, 31168))


"""
최대 N은 8개까지만 사용 가능

N이 number랑 같으면 return 1

combNum = [5, 55, 555 ... 5555555(7개)] 까지 미리 수를 만들어 두고

pool = [ N ] 중복 없애기 위해 SET 사용?

N을 2개 사용했을때부터 8개 사용했을 때까지 반복 (인덱스가 사용한 갯수)
	pool에서 하나 꺼내와서 그걸 가지고 combNum에서 하나씩 가져와서
	반복하여 사칙연산 수행.
	comb = combNum( i - 1 - 1 )
	for target in pool:
		+ =>  target + comb
		-  =>  target - comb
		*  =>  target * comb
		/  =>  target / comb
		각각 결과 값을 담아서 만든 리스트를 만듬
	
	리스트 안에 number가 있는지 확인 -> 있다면, return i

return -1	

"""