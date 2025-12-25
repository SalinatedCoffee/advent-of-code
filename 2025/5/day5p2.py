from bisect import *

INPUT_FNAME = "day5.input"

ans = 0

ranges = []
ids = 0

def add_range(li: list[tuple[int, int]], rng_str: str) -> None:
    s, e = rng_str.split('-')
    ranges.append((int(s), int(e)))

def collate_ranges(li: list[tuple[int, int]]) -> list[tuple[int, int]]:
    li.sort()
    merged = [li[0]]
    for s, e in li:
        if merged[-1][0] <= s <= merged[-1][1]:
            ns, ne = merged.pop()
            merged.append((min(ns, s), max(ne, e)))
        else:
            merged.append((s, e))

    return merged

def verify_id(li: list[int], id_str: str) -> bool:  # TODO
    idx = 0
    while idx < len(li) and li[idx][0] <= int(id_str):
        if int(id_str) <= li[idx][1]:
            return True
        idx += 1
    return False

def count_fresh(li: list[tuple[int, int]]) -> int:
    res = 0
    for s, e in li:
        res += e - s + 1
    return res

with open(INPUT_FNAME) as lines:
    for line in lines:
        line = line.rstrip()
        if line == "":
            break
        add_range(ranges, line)
    ranges = collate_ranges(ranges)
    ans = count_fresh(ranges)

ids = 0

print(f"{ans} fresh items in total.")

