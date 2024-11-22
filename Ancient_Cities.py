from collections import defaultdict

paths = eval(input())
n = int(input())
k = int(input())

visited = [k]

inf = float('inf')

shortest = [inf] * (n+1)

shortest[k] = 0

mat = defaultdict(list)

for u, v, c in paths:
    mat[u].append((v, c))

index = k

while True:
    visited.append(index)
    next_nodes = []
    for v, c in mat[index]:
        next_nodes.append(v)
        if shortest[v] > shortest[index] + c:
            shortest[v] = shortest[index] + c
    
    next_priority = sorted(filter(lambda x: x not in visited, next_nodes), key=lambda x: shortest[x])
    if not len(next_priority):
        break
    index = next_priority[0]

shortest = shortest[1:]

if inf in shortest:
    print(-1)
else:
    print(max(shortest))