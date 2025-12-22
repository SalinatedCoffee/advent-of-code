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
ids = []

def add_range(li: list[tuple[int, int]], rng_str: str) -> None:
    s, e = rng_str.split('-')
    ranges.append((int(s), int(e)))

def collate_ranges(li: list[tuple[int, int]]) -> list[tuple[int, int]]:
    li.sort(key = lambda x: x[0])
    merged = []
    for s, t in li:
        if merged and merged[-1][1] >= s:
            merged[-1][1] = t
        else:
            merged.append((s, t))

    return merged

def verify_id(li: list[int], id_str: str) -> None:
    pass

w_list, w_fun = ranges, add_range

with open(INPUT_FNAME) as lines:
    for line in lines:
        if line == "":
            ranges = collate_ranges(ranges)
            w_list, w_fun = ids, verify_id
            continue
        w_fun(w_list, line)

print(f"{ans}.")

