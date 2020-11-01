"""
r 개만큼을 원소로 갖는 부분집합을 Return하는 것이 아닌, 모든 경우의 수를 한번에 Return

7. 아래와 같은 트리 형태의 경우의 수로 조합을 만들어서 진행함
    A ┬ @
      ├ A' ┬ @
      │    ├ B ┬ @
      │    │   └ C ─ @
      │    └ C ─ @
      ├ B  ┬ @
      │    └ C ─ @
      └ C ─ @
    ...
"""

def combi(before, arr, answer):
    target = before + arr[0]
    arr[0] = '@'

    for i in range(len(arr)):
        if arr[i] == '@':
            if target not in answer:
                answer.append(target)
        else:
            spam = target + arr[i]
            if spam not in answer:
                answer.append(spam)
            combi(target, arr[i:], answer)

    return answer


if __name__ == '__main__':
    # 실험군
    #target = ['1', '2', '3', '4']
    target = ['A', 'A', 'B', 'C']
    answer = []
    for _ in range(len(target)):
        answer = combi('', target, answer)
        target = target[1:]

    answer.sort(key=lambda x : len(x))

    for ans in answer:
        print([x for x in ans])


    print('\n\n')


    # 대조군
    target = ['1', '2', '3', '4']
    from itertools import combinations
    for i in range(len(target)):
        for j in combinations(target, i+1):
            print(j)
        print()