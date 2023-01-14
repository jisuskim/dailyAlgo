def move(stair_list, stair):
    count, d_count = 0, 0
    downstairs = []
    # 이동중인사람이나 대기중인사람, 내려가는 사람이있다면 반복
    while stair_list or downstairs or d_count:
        # 대기 인원이 있는 경우
        while d_count:

            if len(downstairs) == 3:
                break
            # 계단 시간 추가
            downstairs.append(stair[2])
            # 대기인원 감소
            d_count -= 1

        # 내려가는 인원 계산
        for i in range(len(downstairs) - 1, -1, -1):
            # 1초 감소
            downstairs[i] -= 1
            #
            if downstairs[i] <= 0:
                downstairs.pop(i)

        # 이동중인 인원 계산
        for i in range(len(stair_list) - 1, -1, -1):

            stair_list[i] -= 1
            # 계단 도착
            if stair_list[i] <= 0:
                # 대기인원 증가
                stair_list.pop(i)
                d_count += 1
        # 1초 증가 (동시에 3동작 진행)
        count += 1
    return count


def dfs(idx):
    # 조합 확인 후 실행
    if idx == Num:
        global min_count
        stair_A, stair_B = [], []
        # 계단 분리하기
        for i in range(Num):
            if check[i]:
                stair_A.append(Peoples[i][0])
            else:
                stair_B.append(Peoples[i][1])
        # 계단별 시간을 계산하여 더 오래걸리는 계단이 최종 시간이 되도록 함
        count = max(move(sorted(stair_A), Stairs[0]), move(sorted(stair_B), Stairs[1]))
        # 최소 시간과 비교
        min_count = min(count, min_count)
        return
    # B
    check[idx] = False
    dfs(idx + 1)
    # A
    check[idx] = True
    dfs(idx + 1)


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    # 지도 표시, 사람위치, 계단위치
    board, Peoples, Stairs = [], [], []

    # 사람수, 시간
    Num, min_count = 0, float('inf')
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            temp_num = temp[j]
            if temp_num:
                # 사람이면 사람수추가하고 위치추가
                if temp_num == 1:
                    Num += 1
                    Peoples.append([i, j])
                # 계단이라면 계단위치 추가하고 계단길이 추가
                else:
                    Stairs.append([i, j, temp_num])
        board.append(temp)

    # 사람의 계단마다 거리계산
    for i in range(len(Peoples)):
        distance1 = abs(Peoples[i][0] - Stairs[0][0]) + abs(Peoples[i][1] - Stairs[0][1])
        distance2 = abs(Peoples[i][0] - Stairs[1][0]) + abs(Peoples[i][1] - Stairs[1][1])
        Peoples[i][0] = distance1
        Peoples[i][1] = distance2

    # 사람별 계단 정보 저장 A: True, B: False
    check = [False for _ in range(Num)]

    # 백트래킹을 활용한 dfs
    dfs(0)
    print('#{} {}'.format(t, min_count + 1))