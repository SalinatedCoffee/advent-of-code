from math import dist
import heapq
import functools

INPUT_FNAME = 'day8.input'
K = 3
CONNECTIONS = 1000

# Union by size
def merge(a: int, b: int, p: list[int], s: set[int]) -> None:
    # assume a and b are representative nodes of their corresponding sets
    if s[a] > s[b]:
        p[a] = b
        s[b] += s[a]
        del s[a]
    else:
        p[b] = a
        s[a] += s[b]
        del s[b]

def find(a: int, p: list[int]) -> int:
    # No path compression
    pa = p[a]
    while pa != a:
        a = pa
        pa = p[pa]
    return a

junctions = []
with open(INPUT_FNAME) as points:
    for point in points:
        junctions.append(list(map(int, point.rstrip().split(','))))

n = len(junctions)
p = [i for i in range(n)]
s = {i : 1 for i in range(n)}

distances = []
for i in range(n):
    for j in range(i+1, n):
        distances.append([dist(junctions[i], junctions[j]), i, j])
heapq.heapify(distances)

while distances:
    _, a, b = heapq.heappop(distances)
    pa, pb = find(a, p), find(b, p)
    if pa == pb:
        continue
    if s[pa] + s[pb] == n:
        break
    merge(pa, pb, p, s)

print(f'Coordinates for the last two junctions were {junctions[a]} and {junctions[b]}. The product of their x coordinates is {junctions[a][0] * junctions[b][0]}.')

