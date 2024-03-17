# 빗물
# 구현 문제

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):

    left_max = max(blocks[:i])
    right_max = max(blocks[i + 1:])

    standard = min(left_max, right_max)
    depth = blocks[i]

    if standard > depth:
        result += (standard - depth)

print(result)
