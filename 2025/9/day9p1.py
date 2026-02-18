import heapq

INPUT_FNAME = 'day9.input'

tiles = []
with open(INPUT_FNAME) as coords:
    for coord in coords:
        tiles.append(list(map(int, coord.rstrip().split(','))))

# brute force using max heap
n = len(tiles)
areas = []
for i in range(n):
    for j in range(i+1, n):
        areas.append(-1 * (abs(tiles[i][0] - tiles[j][0] + 1) * abs(tiles[i][1] - tiles[j][1] + 1)))
heapq.heapify(areas)

print(f'The area of the largest possible rectangle is {-1 * areas[0]}.')

