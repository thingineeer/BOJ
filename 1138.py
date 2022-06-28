# 한 줄로 서기

N = int(input())
x = list(map(int, input().split()))
d = [0] * N
for i in range(N):
    for j in range(N):
        if x[i] == 0 and d[j] == 0:
            d[j] = i + 1
            break
        elif d[j] == 0:
            x[i] -= 1
print(' '.join(map(str, d)))
