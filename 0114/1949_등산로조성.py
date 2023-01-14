
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(y,x,count,K):
    global ans
    if ans < count+1:
        ans = count+1
    visited[y][x]=1

    for d in range(4):
        nx, ny = x+dx[d],y+dy[d]
        if 0<=nx<N and 0<=ny<N:
            if visited[ny][nx]==0:
                # 공사 필요없이 이동
                if board[ny][nx] < board[y][x]:
                    dfs(ny,nx,count+1,K)
                # 다음 지점에서 공사 진행
                elif board[ny][nx]-K < board[y][x]:
                    temp = board[ny][nx]
                    # 이전 지점의 -1만큼만 깎음
                    board[ny][nx] = board[y][x] -1
                    dfs(ny,nx,count+1,0)
                    board[ny][nx] = temp
    visited[y][x]=0

T = int(input())
for t in range(1, T + 1):
    N, K = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    top = 0
    tops = []
    # 최고 높이 체크 및 저장
    for i in range(N):
        for j in range(N):
            if top < board[i][j]:
                top = board[i][j]
                tops = [[i,j]]
            elif top == board[i][j]:
                tops.append([i,j])

    visited = [[0] * N for i in range(N)]
    # 최고 높이만큼 dfs 진행
    for i in range(len(tops)):
        dfs(tops[i][0],tops[i][1],0,K)

    print('#{} {}'.format(t,ans))