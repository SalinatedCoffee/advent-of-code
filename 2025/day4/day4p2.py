INPUT_FNAME = "day4.input"
VECS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def countAccessibleAndModify(grid):
    res = 0
    m, n = len(grid), len(grid[0])
    modified = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                adj = 0
                for dy, dx in VECS:
                    if (0 <= i+dy < m) and (0 <= j+dx < n) and grid[i+dy][j+dx] == '@':
                        adj += 1
                if adj < 4:
                    modified.append((i, j))
                    res += 1
    for i, j in modified:
        grid[i][j] = '.'
    return res

ans = 0

with open(INPUT_FNAME) as file:
    grid = []
    for line in file:
        grid.append(list(line.rstrip()))
    removed = countAccessibleAndModify(grid)
    ans += removed
    while removed > 0:
        removed = countAccessibleAndModify(grid)
        ans += removed

print(f"Number of accessible rolls: {ans}")

