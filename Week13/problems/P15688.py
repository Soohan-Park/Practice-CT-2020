# 해당 문제는 최적화 문제로 sys.stdin.readline()을 써주면 해결된다. (input()보다 빠름)

import sys

def run():
  #N = int(input())
  N = int(sys.stdin.readline())

  target = [int(sys.stdin.readline()) for _ in range(N)]

  target.sort()

  for t in target: print(t)