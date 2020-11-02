"""
(1,2), (2,3), (3,4), (5,6), (3,2) 가 있을 때, (2,3)을 대칭수라고 한다. ( (2,3) & (3,2) ) 이러한 대칭수를 찾아내는 알고리즘!

>>
1. 좀 더 좋은 효율성을 위해 위 수들을 정렬. (오름차순, 0, 1 인덱스 순으로)
2. 이중 반복문을 통해 순차적으로 탐색한다.
   이 때, 반복 j는 반복 i 인덱스보다 앞의 수를 탐색할 필요는 없다. (이미 탐색되었기 때문)
3. 대칭수 조건에 만족하는 경우 pool에 저장하고, 추후 이를 출력.
"""

def f(target):
  pool = []

  for i in range(0, len(target)-1):  # 맨 마지막 수 탐색 제외
    num1 = target[i]

    for j in range(i+1, len(target)):
      num2 = target[j]

      if num1[0] == num2[1] and num1[1] == num2[0]:  # This is DAECHING-SU!
        pool.append([ num1, num2 ])
  
  for p in pool:
    print(p)


if __name__ == '__main__':
  target = [(1,2), (2,3), (3,4), (5,6), (3,2)]

  target.sort(key=lambda x : (x[0], x[1]))  # Sorted. Because more efficiency.
  
  f(target)