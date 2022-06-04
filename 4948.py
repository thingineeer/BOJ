# 베르트랑 공준

import sys
input = sys.stdin.readline

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

while True:
    n = int(input())
    lst = []
    if n == 0:
        break
    else:
        for i in range(n+1, 2*n+1):
            if is_prime(i):
                lst.append(i)
                
        print(len(lst))