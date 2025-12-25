INPUT_FNAME = "day4.input"
VECS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def countAccessible(grid):
    res = 0
    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                adj = 0
                for dy, dx in VECS:
                    if (0 <= i+dy < m) and (0 <= j+dx < n) and grid[i+dy][j+dx] == '@':
                        adj += 1
                if adj < 4:
                    res += 1
    return res

ans = 0

with open(INPUT_FNAME) as file:
    grid = []
    for line in file:
        grid.append(line)
    ans = countAccessible(grid)

print(f"Number of accessible rolls: {ans}")

