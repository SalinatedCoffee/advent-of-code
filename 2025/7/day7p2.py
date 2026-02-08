# could naively backtrack
# if there are no splitters below particle's current position, backtrack to previous splitter
# no need to keep track of previous path as it is guaranteed to be unique across timelines
# convert manifold into graph, then traverse? alg could be simple recursive DFS thanks to above observation
# how to systematically convert manifold into graph?
# a 'vertex' would correspond to the coordinates of the 'origin' of a split beam
# -> erm, not really
# vertex would be the coords of the splitters
# this means that we need some additional logic for outgoing edges
# a directed edge would exist between vertices a and b if the y coord of a is smaller than b
# and b has x coord (in same column) as either ax-1 or ax+1
# and there are no other vertices between ax-1(or ax+1) and bx in the same column
# generating vertices are easy, traverse manifold
# edges are a bit more tricky
# could just use binary search tho?
# -> this would involve using lists as the underlying data structure
# also remember to add 'sentinel' vertices at the 'end' of each column so that we know when to backtrack
# when to increment timeline counter?
# -> whenever we hit a new splitter
# dictionary of dictionaries of integer tuples
# two pass to generate graph
# first pass records coords of particle origin and splitters in nested lists, in ascending order of respective coords
# -> ex. coords[i] is list of y coords of all splitters in i-th column in ascending order
# second pass generates graph by starting at the origin
# since splitter coords are nicely stored in ascending order (with y coords collected in single lists wrt to columns)
# we can use binary search to determine which splitter a particle would hit next
# on second thought, traversing the resulting graph would be redundant as we can count the number of timelines during
#   the graph generation step

# man, I could have just implemented bottom-up dp
# if we think of the ensuing timelines occurring after a beam runs into a splitter, it's pretty obvious that the resulting subtree is the same regardless of the path that the particle took before to reach it

import bisect

INPUT_FNAME = "test.input"
m, n = 0, 0
ans = 0

def recurse(y: int, x: int, pos: list[list[int]]) -> int:
    return -1

def count_timelines(start: int, pos: list[list[int]]) -> int:
    return -1

with open(INPUT_FNAME) as manifold:
    grid = []
    splitters = []
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

    ans = count_timelines(grid[0].index('S'), splitters)

    print(f'{ans} alternate timelines.')

