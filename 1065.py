cnt = 99
N = input()
if len(N) < 3:
    print(N)
else:
    for i in range(100, int(N) + 1):
        if int(str(i)[0]) + int(str(i)[2]) == 2 * int(str(i)[1]):
            cnt += 1
        else:
            continue
    print(cnt)