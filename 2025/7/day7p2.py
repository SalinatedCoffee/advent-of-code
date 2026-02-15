import bisect
import functools

INPUT_FNAME = "day7.input"
m, n = 0, 0
splitters = []
ans = 0

# top-down DP (memoization)
# can be trivially converted to bottom-up (tabulation), which is left as an exercise to the reader (or myself in the near future)
@functools.cache
def count_timelines(y: int, x: int) -> int:
    timelines = 0
    y = splitters[x][bisect.bisect_left(splitters[x], y)]
    if y == m:
        return 1
    if x > 0:
        timelines += count_timelines(y, x-1)
    if x < n-1:
        timelines += count_timelines(y, x+1)
    return timelines

with open(INPUT_FNAME) as manifold:
    grid = []
    for line in manifold:
        grid.append(line.rstrip())
    m, n = len(grid), len(grid[0])
    for i in range(n):
        col = []
        for j in range(m):
            if grid[j][i] == '^':
                col.append(j)
        col.append(m)
        splitters.append(col)

    sx = grid[0].index('S')
    sy = splitters[sx][bisect.bisect_left(splitters[sx], 0)]
    ans = count_timelines(sy, sx)

    print(f'Counted {ans} alternate timelines.')

