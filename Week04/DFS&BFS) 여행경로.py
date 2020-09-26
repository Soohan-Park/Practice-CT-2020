# DFS - 모든 경로를 방문하고자 할 때

class Graph:
    nodes = dict()
    answer = []

    def __init__(self, _tickets):
        for t in _tickets:
            a = t[0]
            b = t[1]
            keys = self.nodes.keys()

            if a not in keys:
                self.nodes[a] = []
            if b not in keys:
                self.nodes[b] = []


    def addEdge(self, _tickets):
        for t in _tickets:
            a = t[0]
            b = t[1]
            self.nodes[a].append(b)


    def sorting(self):
        for k in self.nodes.keys():
            self.nodes[k].sort()


    def dfs(self, start = "ICN"):
        root = self.nodes[start] # root:list
        self.answer.append(start)

        while len(root) != 0:
            temp = root.pop(0)
            self.answer.append(temp)
            root = self.nodes[temp]


    def print(self):
        return self.answer


def solution(tickets):
    g = Graph(tickets)
    g.addEdge(tickets)
    g.sorting()
    g.dfs()

    return g.print()


if __name__ == '__main__':
    # print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
    print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))