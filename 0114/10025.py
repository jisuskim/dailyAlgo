import sys

N, K = map(int, sys.stdin.readline().split())
ice = [0] * 1111111
left, right = 1111111, 0

temp = []
for i in range(N):
    g, x = map(int, sys.stdin.readline().split())
    temp.append(x)
    ice[x] = g

temp.sort()
left = temp[0]
right = temp[-1]
s_end = left
ans = now = 0

for s_start in range(left, right + 1):
    # 끝 / 좌우 조건 만족
    while s_end < right + 1 and s_end - s_start <= K * 2:
        if not ice[s_end]:
            s_end += 1
            continue
        now += ice[s_end]
        s_end += 1
    ans = max(ans, now)
    now -= ice[s_start]

print(ans)