def dfs(cur, board, visited):
    # 해당 노드에 방문했다고 표시
    visited[cur] = True

    # 연결된 노드들 중 방문하지 않은 곳 탐색
    for i in board[cur]:
        if not visited[i]:
            dfs(i, board, visited)


visited = [ False for _ in range(int(input())) ]
board = dict().fromkeys(range(len(visited)), None)

# 노드별 연결 상태 표시
for _ in range(int(input())):
    f, s = map(int, input().split())
    f = f-1
    s = s-1
    if board[f] is None:
        board[f] = []
    if board[s] is None:
        board[s] = []
    board[f].append(s)
    board[s].append(f)

# 탐색하고자 하는 시작점 노드별 깊이탐색 실행 (여기서는 1개)
dfs(0, board, visited)

print(visited.count(True))
