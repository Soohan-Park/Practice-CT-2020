def run():
  N = int(input())
  weights = list(map(int, input().split()))

  answer = []
  for i in range(1, len(weights)-1):
    dfs(weights.copy(), i, 0, answer)

  print(max(answer))

def dfs(weights, cur, summ, answer):
  summ += weights[cur-1] * weights[cur+1]

  weights.pop(cur)

  if len(weights) > 2:
    for i in range(1, len(weights)-1):
      dfs(weights.copy(), i, summ, answer)
  else:
    answer.append(summ)