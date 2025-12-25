from bisect import *

INPUT_FNAME = "day5.input"

ans = 0

# list of ranges, empty line, list of ids
# if given id is not in any range, it is rotten
# merge ranges
# if ranges can be sorted in order of starting id
# can use binary search to update
# also need to keep track of ending id
# ...or do we?
# since all ranges are merged
# if starting id i is largest id less than some id n
# any range with starting id less than i will never include n
# so the problem now becomes:
# how do we collate given ranges while maintaining their order (ascending by start id)
# 
ranges = []
ids = 0

def add_range(li: list[list[int, int]], rng_str: str) -> None:
    s, e = rng_str.split('-')
    ranges.append([int(s), int(e)])

def collate_ranges(li: list[list[int, int]]) -> list[list[int, int]]:
    li.sort(key = lambda x: x[0])
    merged = [li[0]]
    for s, t in li:
        if s <= merged[-1][1] >= s:
            merged[-1][1] = t
        else:
            merged.append([s, t])

    return merged

def verify_id(li: list[int], id_str: str) -> bool:  # TODO
    idx = 0
    while idx < len(li) and li[idx][0] <= int(id_str):
        if int(id_str) <= li[idx][1]:
            print(li[idx], id_str)
            return True
        idx += 1
    return False

with open(INPUT_FNAME) as lines:
    for line in lines:
        line = line.rstrip()
        if line == "":
            break
        add_range(ranges, line)
    #ranges = collate_ranges(ranges)
    ranges.sort(key = lambda x: x[0])
    #print(ranges)
    for line in lines:
        ids += 1
        ans += 1 if verify_id(ranges, line) is True else 0

print(f"{ans} fresh items out of {ids} total.")

