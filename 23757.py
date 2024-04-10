import heapq

n, m = map(int, input().split())
gift_box = list(map(int, input().split()))
children = list(map(int, input().split()))
box = []

for gift in gift_box: # 많은것부터!
    heapq.heappush(box, -gift)

def gift(children, box):
    
    for child in children:
        b = -heapq.heappop(box)
        
        if b > child:
            heapq.heappush(box, -(b - child))
        elif b == child:
            continue
        else:
            return 0
    return 1

print(gift(children, box))
    