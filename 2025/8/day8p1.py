from math import dist
import heapq
import functools

INPUT_FNAME = 'day8.input'
K = 3
CONNECTIONS = 1000

# Naive union by rank
# Remember that when merging by label like this...
def merge(a: int, b: int, p: list[int], s: list[int]) -> None:
    if a > b:
        p[a] = b
        s[b] += s[a]
    else:
        p[b] = a
        s[a] += s[b]

# ...without path compression...
def find(a: int, p: list[int]) -> int:
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
s = [1 for i in range(n)]

distances = []
for i in range(n):
    for j in range(i+1, n):
        distances.append([dist(junctions[i], junctions[j]), i, j])
heapq.heapify(distances)

merges = 0
while distances and merges < CONNECTIONS:
    merges += 1
    _, a, b = heapq.heappop(distances)
    pa, pb = find(a, p), find(b, p)
    if pa == pb:
        continue
    merge(pa, pb, p, s)
# ...you need to look up set label for each node manually
sets = set([find(i, p) for i in range(n)])
s = [s[i] for i in sets]
# Below line may not work depending on sign in merge()!
# s = [s[i] for i in set(p)]
s.sort(reverse = True)
top_k = s[:K]

print(f'Top {K} sizes were {top_k}, the product of which is {functools.reduce(lambda x, y: x * y, top_k)}.')

