from collections import deque

#입력
n, m, v = map(int, input().split())


graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_d = [0]*(n+1)


def dfs(start): # Dict 자료형 형태로 준다. key는 노드, value는 인접노드를 가리킨다.
    #visited = {i:False for i in graph.keys()} # 방문 배열. visited[node] = True이면 node는 방문이 끝난 상태이다.
    def search(current): # 재귀함수 정의
        visited_d[current] = True # current 방문
        print(current, end= ' ')
        for nxt in graph[current]: # current의 인접 노드를 확인한다. 이 노드를 nxt라고 하자.
            if not visited_d[nxt]: # 만일 nxt에 방문하지 않았다면
                search(nxt) #nxt 방문
    search(start)

visited_b = [0]*(n+1)

def bfs(start): # Dict 자료형 형태로 준다. key는 노드, value는 인접노드를 가리킨다.
    #visited = {i:False for i in graph.keys()} # 방문 배열. visited[node] = True이면 node는 방문이 끝난 상태이다.

    queue = deque([start])
    visited_b[start] = True
    while queue: # 큐가 빌 때까지 반복
        current = queue.popleft() #queue에서 노드를 하나 빼 온다. 이 노드를 current라고 하자.
        print(current, end= ' ')
        for nxt in graph[current]: # current의 인접 노드들을 확인한다. 이 각각의 노드를 nxt라고 하자.
            if not visited_b[nxt]: # 만일 nxt에 방문하지 않았다면
                #nxt 방문
                queue.append(nxt)
                visited_b[nxt] = True
dfs(v)
print("")
bfs(v)
