# A -> B
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
while True:
    if A == B:
        break
    elif (B % 2 != 0 and B % 10 != 1) or A > B:
        print(-1)
        sys.exit(0)
    else:
        if B % 10 == 1:
            B //= 10
            cnt += 1
        else:
            B //= 2
            cnt += 1
print(cnt)