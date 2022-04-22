# 2003번 수들의 합 2

N, M = map(int, input().split())
x = list(map(int, input().split()))

cnt, left, right = 0, 0, 1
while right <= N and left <= right:

    s = sum(x[left:right])
    if s == M:
        cnt += 1
        right += 1
    elif s < M:
        right += 1
    else:
        left += 1
print(cnt)
