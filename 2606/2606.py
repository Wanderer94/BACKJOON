#입력
n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(n+1)

def dfs(start): # Dict 자료형 형태로 준다. key는 노드, value는 인접노드를 가리킨다.
    global cnt
    visited[start] = 1 # 방문 배열. visited[node] = True이면 node는 방문이 끝난 상태이다.
    for nxt in graph[start]: # current의 인접 노드를 확인한다. 이 노드를 nxt라고 하자.
        if not visited[nxt]: # 만일 nxt에 방문하지 않았다면
            dfs(nxt) #nxt 방문
            cnt += 1

dfs(1)
print(cnt)