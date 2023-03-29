#소프트웨어공학 1차과제용 소스코드, 코딩테스트 문제 예시 업로드
from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
graph_g = []
safe_count_list = []
for _ in range(n):
    graph_g.append(list(map(int, input().split())))

graph_original = copy.deepcopy(graph_g)

def findindex_virus_edit(g):
    index_xy=[(i,j) for i in range(n) for j in range(m) if g[i][j]==2]
    return index_xy

def findindex_safetyzone(g):
    index_xy=[(i,j) for i in range(n) for j in range(m) if g[i][j]==0]
    return index_xy

def wall_setup(graph):
    index_list = findindex_safetyzone(graph)

    #print("index_list: ", index_list)
    #print(len(index_list))
    wall_setup_list = list(combinations(index_list, 3))
    #print(len(wall_setup_list))
    for i in range(len(wall_setup_list)): # 경우의 수 6545가지
        graph = copy.deepcopy(graph_original)
        x1, y1 = wall_setup_list[i][0][0], wall_setup_list[i][0][1]
        x2, y2 = wall_setup_list[i][1][0], wall_setup_list[i][1][1]
        x3, y3 = wall_setup_list[i][2][0], wall_setup_list[i][2][1]
        graph[x1][y1] = 1
        graph[x2][y2] = 1
        graph[x3][y3] = 1
        bfs(graph)
        # for i in graph:
        #     print(i)
        # print()
        # 문제점: BFS가 돌아가고 나서 2가 그대로 남아있음
        safe_count_list.append(len(findindex_safetyzone(graph)))


        

def count_safetyzone(g):
    count = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == 0:
                count += 1
    return count

def bfs(graph):
    queue = deque()
    #2인 값만 좌표 넣기
    virus_list = findindex_virus_edit(graph)
    for i in virus_list:
        queue.append((i[0], i[1]))
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 2:
            if (x+1) >= 0 and y >= 0 and x+1 < n and y < m and graph[x+1][y] == 0: #DOWN
                graph[x+1][y] = 2
                queue.append((x+1, y))
            if x >= 0 and (y+1) >= 0 and x < n and y+1 < m and graph[x][y+1] == 0: #RIGHT
                graph[x][y+1] = 2
                queue.append((x, y+1))
            if (x-1) >= 0 and y >= 0 and x-1 < n and y < m and graph[x-1][y] == 0: #UP
                graph[x-1][y] = 2
                queue.append((x-1, y))
            if x >= 0 and (y-1) >= 0 and x < n and y-1 < m and graph[x][y-1] == 0: #LEFT
                graph[x][y-1] = 2
                queue.append((x, y-1))

# print(wall_setup)
# print(findindex_virus(graph))
# bfs(graph_g)
# for i in graph_g:
#     print(i)
wall_setup(graph_g)
print(max(safe_count_list))
