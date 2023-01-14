dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
dir = [0, 2, 1, 4, 3]

T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())

    # board = [[0]*N for _ in range(N)]
    micro = [list(map(int, input().split())) for _ in range(K)]

    for i in range(M):
        # 미생물 번호
        num = -1
        board = [[-1] * N for _ in range(N)]

        # 미생물 별로 이동
        for m in micro:
            y, x, vol, d = m
            num += 1
            # 크기가 0이면 넘김
            if vol == 0:
                continue

            nx, ny = x + dx[d], y + dy[d]
            m[0], m[1] = ny, nx
            # 경계 조건
            if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                m[2] = vol // 2
                m[3] = dir[d]
            # 좌표가 비었을 경우
            if board[ny][nx] == -1:
                board[ny][nx] = [num, vol]
            # 좌표에 이미 미생물이 있을 경우
            else:
                t_num, t_vol = board[ny][nx][0], board[ny][nx][1]
                if t_vol < vol:
                    board[ny][nx] = [num, vol]
                    m[2] += micro[t_num][2]
                    micro[t_num][2] = 0

                else:
                    m[2] = 0
                    micro[t_num][2] += vol

    sum_m = sum(map(lambda x: x[2], micro))
    print('#{} {}'.format(t, sum_m))